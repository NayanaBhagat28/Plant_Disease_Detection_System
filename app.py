import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from class_names import CLASS_NAMES
from disease_info import get_recommendation
import os

MODEL_PATH = "model/plant_model.h5"

st.title("🌱 AI-Based Plant Disease Detection & Recommendation System")

if not os.path.exists(MODEL_PATH):
    st.error("Model not found. Train it first using: python train_model.py")
    st.stop()

model = tf.keras.models.load_model(MODEL_PATH)

uploaded = st.file_uploader("Upload Leaf Image", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Leaf Image", width=400)


    img = img.resize((128,128))
    arr = np.expand_dims(np.array(img)/255.0, axis=0)

    pred = model.predict(arr)
    idx = np.argmax(pred)

    disease = CLASS_NAMES[idx]

# Convert to readable format
    pretty_name = disease.replace("___", " - ").replace("_", " ")

    st.success(f"✅ Disease Detected: {pretty_name}")
    st.info(f"💡 Recommendation: {get_recommendation(disease)}")
