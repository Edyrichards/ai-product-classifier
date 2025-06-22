from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl, Field
from typing import Dict, Any
import uvicorn

# Import the core logic from other project modules
from .scraper import Scraper
from .classifier import VisionClassifier

# --- 1. Initialize FastAPI app ---
app = FastAPI(
    title="AI Product Classifier API",
    description="An API that scrapes a product URL, classifies its image, and returns structured attributes.",
    version="1.0.0"
)

# --- 2. Configure CORS Middleware ---
# This allows the React frontend (running on localhost:3000) to communicate
# with this API (running on localhost:8000).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for simplicity; restrict in production.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (POST, GET, etc.)
    allow_headers=["*"],  # Allows all headers.
)

# --- 3. Define Pydantic Models for Data Validation ---
class URLPayload(BaseModel):
    url: HttpUrl = Field(..., example="https://www.noon.com/uae-en/june-women-viscose-patterned-wide-fit-maxi-dress-green-navy/N53401564A/p/")

class ClassificationAttributes(BaseModel):
    global_attributes: Dict[str, Any] = Field(..., alias="global")
    category_specific_attributes: Dict[str, Any] = Field(..., alias="categorySpecific")

class ClassificationResponse(BaseModel):
    product_title: str = Field(..., alias="productTitle")
    classified_attributes: ClassificationAttributes = Field(..., alias="classifiedAttributes")

# --- 4. Load the AI Model at Startup ---
try:
    classifier = VisionClassifier()
except Exception as e:
    raise RuntimeError(f"Fatal: Could not initialize VisionClassifier. Error: {e}")

# --- 5. Define the API Endpoint ---
@app.post("/api/classify", response_model=ClassificationResponse)
async def classify_product_url(payload: URLPayload, request: Request):
    """
    Orchestrates the entire classification process: scrape, classify, and respond.
    """
    product_url = str(payload.url)
    
    scraped_data = None
    try:
        async with Scraper(headless=True) as scraper:
            results = await scraper.scrape_url(product_url)
            if results:
                scraped_data = results[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred during scraping: {e}")

    if not scraped_data or not scraped_data.get("image_url"):
        raise HTTPException(
            status_code=422,
            detail="Failed to scrape content or find an image at the provided URL."
        )

    product_title = scraped_data.get("product_name", "Title not found")
    image_url = scraped_data.get("image_url")

    try:
        classification_results = classifier.classify_product(image_url)
        if not classification_results:
            raise HTTPException(status_code=422, detail="Classification failed.")

        response_data = {
            "product_title": product_title,
            "classified_attributes": {
                "global": classification_results.get("global", {}),
                "categorySpecific": classification_results.get("categorySpecific", {})
            }
        }
        return response_data

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred during classification: {e}")
