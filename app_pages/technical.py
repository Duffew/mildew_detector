import streamlit as st
import pandas as pd
import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
from pathlib import Path


def show():
    """Displays technical details about the model, including training
    performance metrics, labels distribution, accuracy, loss, and evaluation
    results."""

    st.title("⚙️ Technical Details")
    st.info(
        "This page provides some technical details on the model "
        "training and performance."
    )

    # Labels distribution
    if st.checkbox("Labels Distribution"):  # Fixed typo
        st.header("Labels Distribution", divider=True)
        st.write(
            "The plot below shows the number of images used in train, "
            "validation, and test sets for each label."
        )

        # Improved file path handling
        number_of_images = plt.imread(
            str(Path("outputs/v1/labels_distribution.png"))
        )
        st.image(number_of_images, caption="Number of Images Per Set")

        st.write(
            "As we can see from the count, we had equal numbers of "
            "'healthy' and 'powdery_mildew' images across the train, "
            "test, and validation folders. Had the numbers been unequal, "
            "we would have considered data balancing (oversampling or "
            "undersampling), but that was not required in this project."
        )
        st.write("---")

    # Training accuracy and loss metrics
    if st.checkbox("Accuracy and Loss"):
        st.header("Accuracy and Loss", divider=True)

        # Create columns for side-by-side plot display
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Accuracy")
            st.write(
                "This plot shows the model's accuracy and validation "
                "accuracy across the training epochs."
            )

            accuracy = plt.imread(
                str(Path("outputs/v1/model_training_acc.png"))
            )
            st.image(
                accuracy,
                caption="Accuracy and Validation Accuracy in Training",
            )

        with col2:
            st.subheader("Loss")
            st.write(
                "This plot shows the model's loss and validation "
                "loss across the training epochs."
            )

            loss = plt.imread(
                str(Path("outputs/v1/model_training_losses.png"))
            )
            st.image(loss, caption="Loss and Validation Loss in Training")

        st.write(
            "The above plots show that validation accuracy started "
            "high and remained high across all epochs. It stayed "
            "consistently above training accuracy, which started low "
            "but quickly jumped above 94% and peaked at 98.86% in epoch "
            "6. This suggests rapid learning early in the training. "
            "While validation accuracy remained stable, there were "
            "slight fluctuations in later epochs that might warrant "
            "further investigation."
        )

        st.write(
            "Similarly, the loss values for the training data show rapid "
            "declines as the epochs progressed. Validation loss peaked "
            "in the second epoch at 0.1441, then dropped and mostly "
            "stayed below 0.1, with slight fluctuations. This suggests "
            "confident generalization. As validation losses plateaued, "
            "it is likely that training stopped early due to patience "
            "becoming exhausted."
        )

        st.write(
            "These results suggest that this model is high performing, "
            "learns quickly, and maintains excellent validation accuracy. "
            "Although there are some slight variations in validation loss, "
            "the model seems to generalize well."
        )
        st.write("---")

    if st.checkbox("Model Evaluation"):
        st.header("Model Evaluation", divider=True)

        # Load the evaluation data
        evaluation_path = "outputs/v1/evaluation.pkl"
        with open(evaluation_path, "rb") as file:
            evaluation_array = pickle.load(file)

        # Convert to a labeled dictionary with rounded values
        evaluation_data = {
            "Loss": round(evaluation_array[0], 4),
            "Accuracy": round(evaluation_array[1], 4),
        }

        # Display the results using JSON
        st.json(evaluation_data)

        st.write(
            "The model was evaluated using a set of unseen test data, split "
            "into 106 batches."
        )

        st.write(
            "The saved evaluation returned an accuracy of 0.9965 and a "
            "loss of 0.0877. Both metrics are in line with the validation "
            "figures observed during model fitting."
        )

        st.write(
            "The model exceeds the client's requirement of 97% "
            "accuracy and is well-suited for deployment."
        )
        st.write("---")
