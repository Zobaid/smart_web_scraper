# smart_web_scraper
Web Data Extractor
Overview
Web Data Extractor is a Python-based tool that leverages the power of OpenAI's GPT-3.5 model to extract specific data from web pages. It consists of a Flask API (backend) and a Streamlit UI (frontend), allowing users to easily input a URL and define data extraction schemas.

Features
Data Extraction: Extract specific data from web pages based on user-defined schemas.
Flask API: Robust backend API for processing extraction requests.
Streamlit UI: User-friendly frontend interface for inputting URLs and schema definitions.
GPT-3.5 Integration: Uses OpenAI's powerful language model for accurate data extraction.
Installation
Prerequisites
Python 3.x
Pip (Python package installer)
Setup
Clone the repository:
bash
Copy code
git clone [Your Repository URL]
Navigate to the project directory and install the required packages:
Copy code
pip install -r requirements.txt
Usage
Running the Flask API
Navigate to the api folder.
Run the Flask application:
Copy code
python api.py
Running the Streamlit UI
In a separate terminal, navigate to the frontend folder.
Start the Streamlit application:
arduino
Copy code
streamlit run frontend.py
Interacting with the Application
Open the Streamlit UI in a web browser.
Enter the URL of the web page to extract data from.
Define the schema (attribute names and types).
Submit the form to see the extracted data.
