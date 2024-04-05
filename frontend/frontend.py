import streamlit as st
import requests

st.title('Web Data Extractor')

# Form to input URL and schema
with st.form(key='data_extractor_form'):
    url = st.text_input('Enter the URL')
    attribute_name = st.text_input('Enter the attribute name')
    attribute_type = st.selectbox('Select attribute type', ['text', 'number'])
    submit_button = st.form_submit_button(label='Extract')

if submit_button:
    schema_definition = {
        "attributes": [
            {"name": attribute_name, "type": attribute_type}
        ]
    }

    # Sending POST request to Flask API
    response = requests.post("http://localhost:5000/extract", json={'url': url, 'schema_definition': schema_definition})
    
    if response.status_code == 200:
        st.json(response.json())  # Displaying the response as JSON
    else:
        st.error("Failed to extract data")
