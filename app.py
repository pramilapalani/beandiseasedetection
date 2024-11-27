import streamlit as st

st.title("Bean Disease Detection")
st.write("Upload an image to classify the bean disease.")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Classifying...")
    # Add your model inference code here
    st.write("Predicted Class: Healthy Bean")
