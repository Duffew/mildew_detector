import streamlit as st
# Import custom pages for navigation
from app_pages import home, summary, hypothesis, study, predict, technical

# Define a class object for managing navigation within the Streamlit dashboard.
# This class stores available pages in a structured dictionary, each paired
# with an emoji for improved visual representation in the UI. It enables
# streamlined access to different sections of the application, ensuring a
# user-friendly experience.


class PageManager:
    def __init__(self):
        """Initialize available pages with descriptive emojis.
        Each page corresponds to a key in the dictionary, providing
        easy access to various sections of the dashboard.

        Attributes:
        - pages (dict): A dictionary mapping page names to their
        corresponding functions.
        """

        self.pages = {
            "Home": home.show,  # Landing page for the dashboard
            "Project Summary": summary.show,  # Overview of the project
            "Hypothesis": hypothesis.show,  # Hypothesis and validation
            "Visualization Study": study.show,  # Exploratory data visuals
            "Predict": predict.show,  # Model predictions page
            "Technical": technical.show,  # Technical details
        }

    def run(self):
        """Manage navigation and dynamically load selected pages.

        Displays a sidebar where users can switch between different sections.
        Ensures proper error handling for invalid selections.
        """
        # Sidebar title for easy navigation
        st.sidebar.title("Navigation")

        # Sidebar selection for choosing a page
        selected_page = st.sidebar.radio("Go to:", list(self.pages.keys()))

        # Validate selection and load the corresponding page
        if selected_page in self.pages:
            # Calls the page's function
            self.pages[selected_page]()
        else:
            # Error handling for incorrect selections
            st.error("Page not found. Please select a valid option.")
