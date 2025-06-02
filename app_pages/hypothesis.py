import streamlit as st


def show():
    """
    Displays the hypothesis and validation criteria for mildew detection.

    Functionality:
    - 💡 **Hypothesis**: Describes how a machine learning model can replace
      manual inspection for detecting powdery mildew in cherry leaves.
    - ✅ **Validation**: Outlines the performance assessment approach,
      specifying that the model must achieve at least **97% accuracy** to be
      considered a viable replacement.

    Returns:
    - None
    """

    st.title("💡 Hypothesis")

    st.info(
        "Detection of powdery mildew in cherry leaves currently relies on "
        "manual inspection. We hypothesize that a machine learning model, "
        "trained on images of cherry leaves, could accurately differentiate "
        "healthy leaves from those affected by powdery mildew. This model "
        "could then enable earlier and faster mildew detection."
    )

    st.title("❓ Validation")

    st.warning(
        "The model’s accuracy in detecting powdery mildew will be evaluated "
        "using a labelled test dataset. If accuracy surpasses 97%, "
        "it will be considered a viable replacement for manual "
        "leaf inspection."
    )

    st.title("✅ Conclusion")

    st.success(
        "The technical page provides evidence to prove that the machine "
        "learning model, developed by this project, exceeds the client's "
        "requirement of 97% accuracy and is well-suited to replace "
        "manual leaf inspection."
    )
