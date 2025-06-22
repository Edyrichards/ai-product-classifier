# AI Product Classifier

The AI Product Classifier is a full-stack web application designed to automate the extraction and classification of product attributes from e-commerce websites (specifically Noon.com). It features a React frontend and a Python FastAPI backend.

---

## **1. User Guide**

### **1.1 Interface Overview**

-   **URL Input Form:** The primary area to paste a product URL.
-   **Classify Button:** Starts the analysis process.
-   **Results Display:** Appears below the form to show the structured attributes of the product.

### **1.2 How to Classify a Product**

1.  **Enter URL:** Paste a full product page URL from `Noon.com` into the input field.
2.  **Start Classification:** Click the **Classify** button. A loading indicator will appear while the backend processes the request.
3.  **View Results:** The product's title, global attributes, and category-specific attributes will be displayed in tables.

### **1.3 Error Handling**

If an issue occurs, a descriptive error message will appear (e.g., Invalid URL, Scraping Failure, Internal Server Error).

---

## **2. Setup and Deployment Guide**

### **2.1 Prerequisites**

-   Python 3.8+
-   Node.js 16+ & npm
-   Git

### **2.2 Local Setup**

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/<YOUR_USERNAME>/ai-product-classifier.git
    cd ai-product-classifier
    ```
2.  **Setup Backend:**
    ```sh
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Setup Frontend:**
    ```sh
    cd ../frontend
    npm install
    ```
4.  **Run the application** in two separate terminals:
    -   Terminal 1 (from `backend/`): `uvicorn app.main:app --reload`
    -   Terminal 2 (from `frontend/`): `npm start`
5.  Access the app at `http://localhost:3000`.

---

## **3. API Documentation**

The backend exposes a single REST API endpoint.

### **Endpoint: `/api/classify`**

-   **Method:** `POST`
-   **Description:** Accepts a product URL, scrapes it, classifies the product, and returns structured attributes.

#### **Request Body**

```json
{
  "url": "https://www.noon.com/uae-en/your-product-path/p/"
}
```

#### **Success Response (200 OK)**

```json
{
  "productTitle": "Mock Product - Casual T-Shirt or Sports Shoe",
  "classifiedAttributes": {
    "global": {
      "Type": "T-Shirts",
      "Colour": "Black",
      "Occasion": "Casual"
    },
    "categorySpecific": {
      "Brand": "Uniqlo",
      "Gender": "Men",
      "Material": "Cotton"
    }
  }
}
```

#### **Error Responses**

| Status Code | Meaning                  | Example Detail Message                                |
| :---------- | :----------------------- | :---------------------------------------------------- |
| `422`       | Unprocessable Entity     | "Failed to scrape content from the provided URL."     |
| `500`       | Internal Server Error    | "An internal error occurred during classification."   |
