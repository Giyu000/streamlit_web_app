import streamlit as st
from PIL import Image

st.title('テストアプリ')
st.caption('これは練習用のテストアプリです。')

image = Image.open('./data/python_logo.webp')
st.image(image, width=200)

