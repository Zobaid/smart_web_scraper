# Web Data Extractor

## Overview
Web Data Extractor is a Python-based tool that leverages the power of OpenAI's GPT-3.5 model to extract specific data from web pages. It consists of a Flask API (backend) and a Streamlit UI (frontend), allowing users to easily input a URL and define data extraction schemas.

## Features
- **Data Extraction**: Extract specific data from web pages based on user-defined schemas.
- **Flask API**: Robust backend API for processing extraction requests.
- **Streamlit UI**: User-friendly frontend interface for inputting URLs and schema definitions.
- **GPT-3.5 Integration**: Uses OpenAI's powerful language model for accurate data extraction.

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Setup
1. Clone the repository:
2. Navigate to the project directory and install the required packages:


## Usage

### Running the Flask API
1. Navigate to the `api` folder.
2. Run the Flask application:


### Running the Streamlit UI
1. In a separate terminal, navigate to the `frontend` folder.
2. Start the Streamlit application:


### Interacting with the Application
- Open the Streamlit UI in a web browser.
- Enter the URL of the web page to extract data from.
- Define the schema (attribute names and types).
- Submit the form to see the extracted data.

## Contributing
Contributions to the Web Data Extractor project are welcome. Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments
- OpenAI for the GPT-3.5 model.
- Flask and Streamlit teams for their excellent frameworks.
