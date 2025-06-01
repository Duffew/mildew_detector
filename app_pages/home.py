import streamlit as st


def show():
    """
    Displays the main dashboard page for mildew detection.

    Functionality:
    - Title: Introduces the mildew detection dashboard.
    - Welcome Message: Provides a friendly introduction to the dashboard.
    - Navigation Instructions: Guides users to use radio buttons for site nav.
    - Encourages Engagement: Makes the dashboard experience more interactive.

    Returns:
    - None
    """

    st.title("🏠 Mildew Detection Dashboard")
    st.markdown(
        """Welcome to this Streamlit dashboard dedicated to mildew analysis!
        Use the radio buttons on the left to navigate the site.
        Have fun!"""
    )
    