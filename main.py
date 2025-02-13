import requests
import streamlit as st
# import pandas as pd

url = 'https://api.nasa.gov/planetary/apod?api_key=YJhjhLUJNuTI7NIerE0nddxKwrAqgC2MYFTWy770'

response = requests.get(url)
content = response.json()

title = content['title']
explanation = content['explanation']
image_url = content['hdurl']

image = requests.get(image_url)

st.set_page_config("Astronaut Damola", layout='centered')
st.title(title)
st.image(image.content)
st.write(explanation)