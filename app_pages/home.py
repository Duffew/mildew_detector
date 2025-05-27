import streamlit as st

def show():
    """
    Displays the main dashboard page for mildew detection.

    Functionality:
    - 🚀 **Title:** Introduces the mildew detection dashboard.
    - 👋 **Welcome Message:** Provides a friendly introduction to the dashboard.
    - ⬅️ **Navigation Instructions:** Guides users to use radio buttons for site navigation.
    - 🎉 **Encourages Engagement:** Makes the dashboard experience more interactive and enjoyable.

    Streamlit Components Used:
    - `st.title()` → Displays the main heading.
    - `st.markdown()` → Formats a welcome message with emojis for a user-friendly experience.

    Returns:
    - None
    """

    st.title("🚀 Mildew Detection Dashboard")
    st.markdown("""
    👋 Welcome to the Streamlit dashboard for analysing mildew detection in cherry leaves!  
                
    ⬅️ Use the radio buttons on the left-hand side of the browser to navigate the site.  
                
    🎉 Have fun!
    """)
    
    