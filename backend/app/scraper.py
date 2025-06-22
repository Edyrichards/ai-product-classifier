import time
import logging
from typing import List, Dict, Any

logger = logging.getLogger("MockScraper")

class Scraper:
    """
    A mock class that simulates the behavior of a web scraper.
    It returns hardcoded data to allow API testing without real web requests.
    """
    def __init__(self, headless: bool = True, timeout: int = 10000):
        """Initializes the mock Scraper."""
        self.headless = headless
        self.timeout = timeout
        logger.info("Initializing Mock Scraper...")

    async def __aenter__(self):
        """Mimics the async context manager entry for launching a browser."""
        logger.info("Mock Browser launched.")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Mimics the async context manager exit for closing a browser."""
        logger.info("Mock Browser closed.")

    async def scrape_url(self, url: str) -> List[Dict[str, Any]]:
        """
        Simulates scraping a single product page URL.
        """
        logger.info(f"Mock-scraping URL: {url}")
        time.sleep(0.1) # Simulate network and page load time

        mock_product_data = {
            "product_name": "Mock Product - Casual T-Shirt or Sports Shoe",
            "price": 99.99,
            "discount": "10%",
            "delivery_info": "Ships in 2 days",
            "image_url": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?q=80&w=1000",
        }
        
        logger.info("Successfully mock-scraped product data.")
        return [mock_product_data]
