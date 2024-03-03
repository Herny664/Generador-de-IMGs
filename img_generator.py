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

def download_image(img, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)

# Configuración de la app web
st.set_page_config(page_title="Simple IMG Generator", page_icon="👾", layout="centered")
# Creación de la app web
st.image("img/futuristic-city-landscape.jpg", use_column_width=True)
st.title("Simple AI Image Generator")
# Agregando Sidebar
description = st.text_area("Prompt")
# Agregando Botón
if st.button("Generate Image"):
    with st.spinner("Generating your image..."):
        url = openai_request(description)
        filename = "AI_images/image_generator.png"
        download_image(url, filename)
        st.image(filename, use_column_width=True)
        with open(filename, "rb") as f:
            image_data = f.read()
        download = st.download_button(label="Download Image", data=image_data, file_name="image_generated.jpg")