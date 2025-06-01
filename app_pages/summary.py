import streamlit as st


def show():
    """
    Displays the project summary page for mildew detection in cherry trees.

    This function presents the key information about the project, including:
    - Project Background: Explanation of powdery mildew affecting cherry trees.
    - Project Dataset: Description of the dataset containing leaf images.
    - Business Requirements: Goals of the client, including image analysis
    and machine learning predictions.
    - Further Reading: Additional resources for understanding powdery
    mildew and its impact.

    Returns:
        None
    """

    st.title("📜 Project Summary")
    st.header("🌳 Project Background", divider=True)
    st.write("""
    Cherry trees are susceptible to a fungus known as podosphaera clandestine,
             which presents as a powdery mildew.

    - Fungus spores, which winter on or close to the trees, are released
             in response to rain or irrigation and attach themselves to
             leaves or new shoots.
    - The spores are most active during the spring, and an infected tree
             will show signs of mildew within 4-6 weeks of new buds breaking.
    - Powdery mildew usually appears on the leaves of cherry trees and
             may also be present on stems and the fruit.
    - If left untreated, powdery mildew will reduce the yield of a
             cherry tree, is contagious for other plants, and will become
             a perennial problem.
    """)

    st.header("🗂️ Project Dataset", divider=True)

    st.write("""
    - The project makes use of images of cherry leaves categorized as
               either ‘healthy’ or suffering from ‘powdery mildew’.
    - There are **2,104 images** in each category.
    """)

    st.header("💼 Business Requirements", divider=True)
    st.write("""
    - The client would like to see a study of the images.
    - The client would like to see a machine learning prediction on
               whether an image of a cherry leaf shows a
               healthy leaf or mildew-affected.
    """)

    st.header("📖 Further Reading", divider=True)
    st.write("""
    - [Mildew Detector Business Case](https://bit.ly/3SyqucG)
    - [Powdery Mildew in Sweet Cherries](http://bit.ly/4mGgRGL)
    - [Powdery Mildew Information](https://bit.ly/43F0p0N)
    """)
