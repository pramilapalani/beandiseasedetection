# Save this in a file named `app.py`
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model("beans_model.keras")

# Class labels
class_names = ['Angular Leaf Spot', 'Bean Rust', 'Healthy']

# Image preprocessing function for prediction
def preprocess(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

# Streamlit app
st.title("Bean Disease Classifier")
st.write("Upload an image of a bean leaf to classify its health.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Classifying...")
    processed_image = preprocess(image)
    predictions = model.predict(processed_image)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions)
    st.write(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}")
