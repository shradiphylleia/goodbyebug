# either locally or the image from the camera
import streamlit as st

def image_upload():
    choice=st.radio("Upload image from",["device","camera"])
    if choice=="device":
        uploaded_file = st.file_uploader("Choose an image file", type="jpg")
        if uploaded_file:
            st.image(uploaded_file)

    else:
        uploaded_file=st.camera_input("take a picture")

