# AI Product Classifier

This is a full-stack application designed to scrape product information from an e-commerce website, classify its attributes using an AI model, and present the data through a web interface.

The project consists of a **FastAPI** backend that handles the web scraping and API logic, and a **React** frontend for the user interface.

---

### Prerequisites

Before you begin, ensure you have the following installed on your system:
- **Python 3.8+**
- **Node.js v14+** (which includes npm)
- **Git**

---

### **Setup Instructions**

Follow these steps to get your development environment set up.

**1. Clone the Repository**
Open your terminal and clone the project repository using the following command:
```shell
git clone https://github.com/Edyrichards/ai-product-classifier.git
2. Navigate to the Project Directory

cd ai-product-classifier
3. Set Up the Python Virtual Environment It is a best practice to create a virtual environment to manage the project's Python dependencies separately.

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
.\venv\Scripts\activate
You will know the environment is active when you see (venv) at the beginning of your terminal prompt.

4. Install Backend Dependencies Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt
5. Install Playwright Browsers The backend uses Playwright for web scraping, which requires browser binaries to be downloaded. Run the following command to install them:

playwright install
This command downloads the necessary browsers (like Chromium, Firefox, and WebKit) for Playwright to function correctly.

Running the Application
You will need two separate terminal windows to run the backend and frontend servers simultaneously.

Terminal 1: Run the Backend Server (FastAPI)

Make sure you are in the project's root directory (ai-product-classifier) and your virtual environment is activated (source venv/bin/activate).
Navigate to the backend directory.
cd backend
Start the FastAPI server using Uvicorn.
uvicorn api_server:app --reload
The --reload flag automatically restarts the server when you make changes to the code. Your API is now running and accessible at http://127.0.0.1:8000.
Terminal 2: Run the Frontend Application (React)

Open a new terminal window and navigate to the project's root directory (ai-product-classifier).
Navigate into the frontend directory.
cd frontend
Install the necessary Node.js packages.
npm install
Start the React development server.
npm start
Your frontend application will automatically open in your default web browser, accessible at http://localhost:3000.

---
