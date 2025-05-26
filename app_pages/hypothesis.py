import streamlit as st

def show():
    st.title("💡 Hypothesis")
    
    st.info("The detection of powdery mildew in cherry leaves currently " \
    "relies on manual inspection. It is our hypothesis that a machine " \
    "learning model, trained on images of cherry leaves, could accurately " \
    "differentiate between images of healthy leaves and those affected by " \
    "powdery mildew. This model could then allow for earlier and faster " \
    "mildew detection.")

    st.title("✅ Validation")
    st.success("The model’s accuracy in detecting powdery mildew will be " \
    "evaluated using a labelled test dataset. If the model's accuracy passes " \
    "97%, it will be considered a viable replacement for manual leaf " \
    "inspection.")