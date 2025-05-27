import streamlit as st

def show():
    """
    Displays the project summary page for mildew detection in cherry trees.

    This function presents the key information about the project, including:
    - 🌳 **Project Background**: Explanation of powdery mildew affecting cherry trees.
    - 🖼️ **Project Dataset**: Description of the dataset containing cherry leaf images.
    - 💼 **Business Requirements**: Goals of the client, including image analysis and machine learning predictions.
    - 📖 **Further Reading**: Additional resources for understanding powdery mildew and its impact.

    Streamlit Components Used:
    - `st.title()` → Displays the main heading.
    - `st.subheader()` → Creates section headers for better organization.
    - `st.info()` → Provides informational highlights about powdery mildew.
    - `st.warning()` → Displays dataset details with an alert-style box.
    - `st.success()` → Highlights key business requirements.
    - `st.error()` → Provides additional reading resources in an emphasized format.

    Returns:
        None
    """

    st.title("📜 Project Summary")
    
    st.subheader("🌳 Project Background")
    st.info("""
    Cherry trees are susceptible to a fungus known as podosphaera clandestine, which presents as a powdery mildew.
    
    - 🌧️ Fungus spores, which winter on or close to the trees, are released in response to rain or irrigation and attach themselves to leaves or new shoots.
    - 🌱 The spores are most active during the spring, and an infected tree will show signs of mildew within 4-6 weeks of new buds breaking.
    - 🍀 Powdery mildew usually appears on the leaves of cherry trees and may also be present on stems and the fruit.
    - ⚠️ If left untreated, powdery mildew will reduce the yield of a cherry tree, is contagious for other plants, and will become a perennial problem.
    """)

    st.subheader("🖼️ Project Dataset")
    st.warning("""
    - 🍀 The project makes use of images of cherry leaves categorized as either ‘healthy’ or suffering from ‘powdery mildew’.  
    - 📷 There are **2,104 images** in each category.
    """)

    st.subheader("💼 Business Requirements")
    st.success("""
    - 🔎 The client would like to see a study of the images.
    - 🤖 The client would like to see a machine learning prediction on whether an image of a cherry leaf shows a healthy leaf or mildew-affected.
    """)

    st.subheader("📖 Further Reading")
    st.error("""
    - 📄 [Mildew Detector Business Case](https://github.com/Duffew/mildew_detector/tree/main#ml-business-case-assessment)  
    - 🍒 [Powdery Mildew in Sweet Cherries](https://www.bctfpg.ca/pest_guide/info/101/Powdery_Mildew_Sweet_Cherries#:~:text=Powdery%20mildew%20of%20cherry%20is%20caused%20by%20the%20fungus%20Podosphaera%20clandestina.&text=On%20leaves%2C%20powdery%20mildew%20appears,often%20puckered%20or%20distorted%20(Fig.))  
    - 🌱 [Powdery Mildew Information](https://www.wmmga.org/content.aspx?page_id=22&club_id=101643&module_id=228931#:~:text=If%20you've%20had%20powdery,resistant%20varieties%20have%20been%20developed.)  
    """)