import time
import random

class VisionClassifier:
    """
    A mock class that simulates the behavior of the real VisionClassifier.
    It returns pre-defined, structured data without needing an actual AI model.
    """
    def __init__(self, model_name: str = "mock/clip-model"):
        """
        Simulates the initialization of the classifier.
        """
        print("Initializing Mock Vision Classifier...")
        time.sleep(0.1) # Simulate a small delay for model loading
        print(f"Mock model '{model_name}' is ready.")
        self.device = "cpu"

    def classify_product(self, image_url: str) -> dict:
        """
        Simulates the classification of a product image from a URL.
        """
        print(f"Mock-classifying image from: {image_url}")
        time.sleep(0.2) # Simulate network and processing time

        # Randomly return one of two mock responses to show variability
        if random.random() > 0.5:
            # Mock response for a T-Shirt
            print("  - Mock prediction: T-Shirt")
            return {
                "global": {
                    "Type": "T-Shirts",
                    "Colour": "Black",
                    "Occasion": "Casual"
                },
                "categorySpecific": {
                    "Brand": "Uniqlo",
                    "Gender": "Men",
                    "Material": "Cotton",
                    "Style": "Basic",
                    "Fit": "Regular Fit",
                    "Pattern": "Solid",
                    "Neck Type": "Crew Neck",
                    "Sleeve Type": "Short Sleeve"
                }
            }
        else:
            # Mock response for Sports Shoes
            print("  - Mock prediction: Sports Shoes")
            return {
                "global": {
                    "Type": "Sports Shoes",
                    "Colour": "White",
                    "Occasion": "Sports"
                },
                "categorySpecific": {
                    "Brand": "Nike",
                    "Gender": "Unisex",
                    "Material": "Synthetic",
                    "Style": "Sneakers",
                    "Closure Type": "Laces",
                    "Sports Type": "Running",
                    "Performance Feature": "Cushioning",
                }
            }
