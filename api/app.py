import openai
import requests
from bs4 import BeautifulSoup
import re
from flask import Flask, request, jsonify


app = Flask(__name__)


# Set up the OpenAI API credentials
openai.api_key = "api key"

def preprocess_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text[:2000]  # Adjust this value based on token limits
    return text

def extract_data(url, schema_definition):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    webpage_text = preprocess_text(soup.get_text())

    extracted_data = {}
    for attribute in schema_definition['attributes']:
        prompt = f"Extract the {attribute['name']} as a {attribute['type']} from the following text: {webpage_text}"

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-0125",  # Updated to a newer model
            prompt=prompt,
            max_tokens=100
        )

        extracted_value = response.choices[0].text.strip()
        if attribute['type'] == 'number':
            try:
                extracted_value = float(extracted_value)
            except ValueError:
                extracted_value = None  # Handle non-numeric extraction
        extracted_data[attribute['name']] = extracted_value

    return extracted_data


@app.route('/extract', methods=['POST'])
def extract():
    data = request.json
    url = data['url']
    schema_definition = data['schema_definition']
    extracted_data = extract_data(url, schema_definition)
    return jsonify(extracted_data)

if __name__ == '__main__':
    app.run(debug=True)
# if __name__ == "__main__":
#     url = input("Enter the webpage URL: ")
#     schema_definition = {"attributes": []}
#     while True:
#         attribute_name = input("Enter the name of an attribute (or 'done' to finish): ")
#         if attribute_name.lower() == 'done':
#             break
#         attribute_type = input(f"Enter the type of attribute '{attribute_name}' (text/number): ")
#         schema_definition["attributes"].append({"name": attribute_name, "type": attribute_type})

#     extracted_data = extract_data(url, schema_definition)
#     print("Extracted data:")
#     print(extracted_data)
