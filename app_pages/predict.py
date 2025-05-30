import streamlit as st
import tensorflow as tf
import pandas as pd
from PIL import Image
import numpy as np

def predict(image):
    """
    Processes uploaded images and predicts whether leaves are affected by powdery mildew.

    Steps:
    1. Loads the trained mildew detection model.
    2. Preprocesses images:
       - Resizes to match training dimensions (128 by 128).
       - Converts to a normalized NumPy array (values scaled between 0 and 1).
       - Adds a batch dimension for TensorFlow model compatibility.
    3. Runs images through the model to obtain a probability score.
    4. Extracts the raw probability, ensuring proper formatting.
    5. Applies a classification threshold (0.5):
       - If probability < 0.5 → "Healthy" leaf.
       - If probability ≥ 0.5 → "Powdery Mildew."
    6. Inverts the probability mapping for "Healthy" classifications to ensure correct confidence display.
    7. Returns the predicted label and confidence percentage.

    Args:
        image (file-like object): The uploaded leaf image in JPG or PNG format.

    Returns:
        tuple: (classification label, confidence score)
               - Label: "Healthy" or "Powdery Mildew."
               - Confidence: Adjusted probability ensuring meaningful confidence representation.
    """
    
    # Load the fitted model from the keras file
    model = tf.keras.models.load_model("outputs/v1/mildew_detector_model.keras")

    # Preprocess image to match training size (128×128)
    img = Image.open(image).resize((128, 128))
    # Convert image to numpy array and normalise pixel values
    img_array = np.array(img) / 255.0 
    # Add batch size to image shape for tensorflow processing
    img_array = np.expand_dims(img_array, axis=0)

    # Predict on uploaded images
    prediction = model.predict(img_array)
    # Extract the raw probability from the nested array - remove brackets
    raw_value = prediction[0][0]
    # Format the debug output for Streamlit - show 7 decimal places
    debug_output = f"Raw Model Output (Mildew Probability): {raw_value:.7f}"
    # Display 'Raw Model Output' in Streamlit as a text block
    st.text(debug_output)  
    # Extract probability correctly
    probability = float(prediction[0][0])

    # Assign label based on probability threshold
    label = "Healthy" if probability < 0.5 else "Powdery Mildew"

    # Invert probability mapping for leaves labeled as 'Healthy'
    # Example: 0.04 confidence becomes 0.96
    confidence = 1 - probability if label == "Healthy" else probability

    return label, confidence

def show():
    st.title("🤖 Predict Cherry Leaf Health")
    st.write("Upload cherry leaf images for AI-powered analysis.")

