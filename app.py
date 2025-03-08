# learn how to build a isolated environment
import streamlit as st
from imgUpload import image_upload

st.logo("bug.png")
st.header("goodbyebug 🐛")
st.write("upload and image and get to know which pest is it that is bothering your farm!")

st.subheader("upload an image.")
st.write("images in good light will show better results")

image_upload()

