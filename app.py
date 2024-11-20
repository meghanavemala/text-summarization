import streamlit as st
import requests
import os
#from dotenv import load_dotenv

# Load environment variables from .env file
#load_dotenv()

# Set Cohere API key from environment variables
cohere_api_key = "9cXeu16WbLhcKXpfCjJspMsN9WLQY5zEIIaw77BB"  # Replace with your actual Cohere API key

# Function to summarize text using Cohere API
def summarize_text(text):
    url = "https://api.cohere.ai/generate"
    
    headers = {
        "Authorization": f"Bearer {cohere_api_key}",
        "Content-Type": "application/json"
    }
    
    # Prepare the data for the API request
    data = {
        "model": "command",  # Use the appropriate Cohere model for summarization
        "prompt": f"Summarize the following text:\n\n{text}\n\nSummary:",
        "max_tokens": 100,  # Adjust based on the desired length of the summary
        "temperature": 0.3,  # Lower temperature for more focused summaries
        "stop_sequences": ["\n"]  # Define where the output should stop
    }
    
    try:
        # Send the request to Cohere's API
        response = requests.post(url, json=data, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the response JSON
            response_data = response.json()
            
            # Check if 'text' is in the response
            if 'text' in response_data:
                return response_data['text'].strip()
            else:
                return f"Error: 'text' key not found in response. Response: {response_data}"
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize Streamlit app
st.set_page_config(page_title="Text Summarization with Cohere")
st.header("Text Summarization using Cohere API")

# Input box for the user's text
input_text = st.text_area("Enter the text to summarize:", key="input")

# Button to trigger the summarization
submit = st.button("Summarize")

# If the button is clicked and the input text is not empty
if submit and input_text:
    summary = summarize_text(input_text)
    st.subheader("Summary:")
    st.write(summary)
