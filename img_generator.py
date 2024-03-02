import requests
import streamlit as st

api_key = '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'

def openai_request(prompt):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers=headers,
        json={
            'prompt': prompt,
            'model': 'dall-e-3',
            'size': '1024x1024',
            'quality': 'standard',
            'n': 1
        }
    )
if response.status_code != 200:
    raise Exception(response.json())
else:
    image_url = response.json()['data'][0]['url']

return image_url