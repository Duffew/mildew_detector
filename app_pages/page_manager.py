import streamlit as st
# Import custom pages for structured navigation
from app_pages import summary, hypothesis, study, predict, technical  

class PageManager:
    def __init__(self):
        """Initialize available pages with descriptive emojis.

        Each page corresponds to a key in the dictionary, making navigation simple.
        The emoji improves user engagement and visual clarity.
        """
        self.pages = {
            "📜 Project Summary": summary.show,  # Overview of the project
            "🔬 Hypothesis": hypothesis.show,    # Research-based assumptions
            "📊 Visualization Study": study.show, # Exploratory data visuals
            "🤖 Predict": predict.show,          # Model predictions page
            "⚙️ Technical": technical.show,      # Deep-dive into technical details
        }

    def run(self):
        """Manage navigation and dynamically load selected pages.

        Displays a sidebar where users can switch between different sections.
        Ensures proper error handling for invalid selections.
        """
        st.sidebar.title("🔀 Navigation")  # Sidebar title for easy navigation
        
        # Sidebar selection for choosing a page
        selected_page = st.sidebar.radio("Go to:", list(self.pages.keys()))

        # Validate selection and load the corresponding page
        if selected_page in self.pages:
            self.pages[selected_page]()  # Calls the associated page's function
        else:
            st.error("❌ Page not found. Please select a valid option.")  # Error handling for incorrect selections