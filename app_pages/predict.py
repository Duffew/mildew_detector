import streamlit as st
import tensorflow as tf
import pandas as pd
from PIL import Image
import numpy as np

def predict(image):
    """
    Processes uploaded images and predicts whether leaves are affected by 
    powdery mildew.

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
    6. Inverts the probability mapping for "Healthy" classifications 
    to ensure correct confidence display.
    7. Returns the predicted label and confidence percentage.

    Args:
        image (file-like object): The uploaded leaf image

    Returns:
        tuple: (classification label, confidence score)
               - Label: "Healthy" or "Powdery Mildew."
               - Confidence: Adjusted probability ensuring meaningful 
               confidence representation.
    """
    
    # Load the fitted model from the keras file
    model = tf.keras.models.load_model("outputs/v1/mildew_detector_model.keras")

    # Preprocess image to match training size (128×128)
    img = Image.open(image).resize((128, 128))
    # Convert image to numpy array and normalise pixel values
    img_array = np.array(img) / 255.0 
    # Add batch size to image shape for tensorflow processing
    img_array = np.expand_dims(img_array, axis=0)

    # Predict on uploaded image
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
    # Example: 0.04 confidence of 'powdery mildew' 
    # becomes 0.96 confidence of 'healthy'
    confidence = 1 - probability if label == "Healthy" else probability

    return label, confidence

def show():
    
    st.title("🤖 Predict Cherry Leaf Health")
    st.info("""
            Welcome to the inference page! Here you can:
            
            - Upload multiple cherry leaf images to the machine learning model, 
            and it will make a prediction about the health of the leaves.

            - Download a summary of results as a .csv file.  

            - If you don't have any images of cherry leaves to hand, 
            you can download some below.
            """)
    
    # Download
    st.header("📥 Download Images", divider=True)

    # Download link for cherry leaf images
    st.markdown("[Download Cherry Leaf Images](" \
    "https://www.kaggle.com/datasets/cameronconroy/cherry-leaves-test-data)")
    
    
    # Upload
    st.header("📤 Upload Images", divider=True)

    # File upload widget for multiple images
    uploaded_files = st.file_uploader("Upload cherry leaf images for " \
    "AI-powered analysis. You can upload multiple images.", 
    type=["jpg", "png"], accept_multiple_files=True)

    if uploaded_files:
        results = []
        for file in uploaded_files:
            st.image(file, caption=file.name, width=200)
            label, prob = predict(file)

            # Show only the classification statement with confidence level
            st.write(f"Classification: **{label} ({prob:.2%} confidence)**")

            results.append({"Image Name": file.name, "Prediction": label,
                             "Confidence Level": f"{prob:.2%}"})

        # Convert results to DataFrame
        st.header("📊 Results", divider=True)
        df = pd.DataFrame(results)
        st.dataframe(df)

        # Download button for results
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Predictions", csv, 
                           "predictions.csv", "text/csv")