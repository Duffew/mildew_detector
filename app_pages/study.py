import streamlit as st
import matplotlib.pyplot as plt
import random
from pathlib import Path

def image_montage(selection):
    """
    Displays a random montage of cherry leaves categorized as 'healthy' or 
    'powdery mildew' within a Streamlit dashboard. This function dynamically 
    selects and arranges images in a structured 3x3 grid format while providing 
    a refresh button for users to generate a new random selection.

    Functionality:
    - Accepts user-selected leaf type ('Healthy' or 'Powdery Mildew') via 
    radio buttons.
    - Dynamically retrieves images from predefined directories using Pathlib.
    - Ensures images persist across selections using Streamlit session state.
    - Displays the images in a clean, structured 3x3 grid layout.
    - Provides a refresh button to generate a new random selection.
    - Formats UI elements to maintain intuitive interaction and alignment.

    Parameters:
    - selection (str): The category of leaves ('Healthy' or 'Powdery Mildew') 
    chosen by the user.
    """
    
    # Define input image paths
    test_path = Path(f"inputs/cherry-leaves/cherry-leaves/test/{
        selection.lower().replace(' ', '_')}")

    if not test_path.exists():
        st.warning("⚠️ Directory not found. Please check your file paths.")
        return

    image_paths = list(test_path.glob("*.*"))

    if not image_paths:
        st.warning(f"⚠️ No images found in '{selection}' directory.")
        return

    # Reset images when radio button selection changes
    if "montage_selection" not in st.session_state or st.session_state[
        "montage_selection"] != selection:
        st.session_state["montage_selection"] = selection
        st.session_state["montage_images"] = random.sample(
            image_paths, min(9, len(image_paths)))

    # Title and Refresh button placement
    col1, col2 = st.columns([4, 1])
    # Column 1 has 4 units width for Title
    with col1:
        st.subheader(f"Currently viewing {selection.lower()} leaves")
    # Column 2 has 1 unit width for Refresh button
    with col2:
        if st.button("🔄 Refresh Montage"):
            st.session_state["montage_images"] = random.sample(
                image_paths, min(9, len(image_paths)))
    

    selected_images = st.session_state["montage_images"]

    # Display images in a 3x3 grid layout
    cols = st.columns(3)
    for idx, img in enumerate(selected_images):
        with cols[idx % 3]:
            st.image(str(img), use_container_width=True)


def show():
    """
    Displays an interactive visualization study within the Streamlit dashboard,
    allowing users to see differences between healthy cherry leaves and those 
    affected by powdery mildew.

    Functionality:
    - Presents an overview of the visualization study.
    - Allows users to explore image comparisons via checkboxes.
    - Uses Pathlib for structured file path handling.
    - Displays images of leaf variability and average differences.
    - Provides an option to generate an image montage.
    """

    def data_visual_body():
        """
        Handles the visualization study's interactive elements, including 
        image selection and comparison options.

        Functionality:
        - Displays an overview of the study with contextual information.
        - Provides checkboxes for users to selectively view:
            - Average and variability images for healthy and mildewed leaves.
            - The difference between average healthy and mildewed images.
            - A randomized image montage of selected leaf categories.
        - Uses Pathlib for structured file path management and test.
        - Ensures smooth image loading and warns users if images are missing.
        - Utilizes radio buttons for selecting image categories.
        - Passes user selections to `image_montage()` for dynamic image display.
        """

        # Title
        st.title("🔬 Visualization Study")

        # Instructions
        st.info("""The client requires a study that displays the differences
        between healthy cherry leaves and those infected with powdery mildew.

        Select from the checkboxes below to visualize the image data.""")

        # Define Paths Using Pathlib
        out_path = Path("outputs/v1")
        avg_healthy_path = out_path / "avg_var_healthy.png"
        avg_mildew_path = out_path / "avg_var_powdery_mildew.png"
        avg_diff_path = out_path / "avg_diff_healthy_powdery_mildew.png"

        # Checkbox: Average and Variability Images
        if st.checkbox("The difference between average and variability images"):

            st.header('🔍 Variability Images Analysis', divider=True)
            st.subheader('🌿 Healthy Leaves')
            st.success("""
            
            Healthy Leaves
                       
            - The average healthy leaf looks to have a relatively consistent shade of green suggesting even chlorophyll distribution.
            - The variation image for healthy leaves shows a black centre with minimal gren hue, shifting to a purple ring at the edge.
            
            This suggests:
                       
            - Minimal to no variance in healthy leaves at the centre.
            - Greater variance in healthy leaves towards the edge.
                       
            Conclusion:
            
            Healthy cherry leaves will show little if any meaningful difference in appearance at their centres 
            but greater differences at their edges.
                       
            """)

            # Healthy variability image
            if avg_healthy_path.exists():
                average_healthy = plt.imread(str(avg_healthy_path))

                healthy_caption = 'Healthy Leaf - Average and Variability'
                st.image(average_healthy, caption=healthy_caption)             
            else:
                st.warning(
                    "⚠️ Image file not found. Please check your file paths.")

            st.write("---")

            st.subheader('🦠 Mildewed Leaves')
            st.success("""
            
            Mildewed Leaves
                       
            - The average mildewed leaf looks to have a blotchy appearance and lighter shade indicating chlorophyll depletion.
            - The variation image for mildewed leaves shows a greenish hue in the centre becoming a subdued purple ring towards the edge. 
                       
            This suggests:
                
            - Some variance across mildewed leaves at the centre - greater than that of a healthy leaf.
            - Greater variance in mildewed leaves towards the edge.
                       
            Conclusion:
            
            Cherry leaves infected with powdery mildew exhibit similar characteristics at the centre of the leaf, 
            albiet with some variations. The variances at the centre, however, are less pronounced 
            than those at the edges of leave, where the variance is greatest. 
                        
            """)


            if avg_mildew_path.exists():
                average_mildew = plt.imread(str(avg_mildew_path))

                mildew_caption = 'Mildewed Leaf - Average and Variability'
                st.image(average_mildew, caption=mildew_caption)
            else:
                st.warning(
                    "⚠️ Image files not found. Please check your file paths.")

            st.write("---")

        # Checkbox: Difference Between Average Healthy & Mildewed Leaves
        if st.checkbox(
            "The difference between the average healthy and mildewed leaves"):

            st.header('🔍 Average Images Analysis', divider=True)
            st.success("""
                       
            - The average healthy leaf looks to have a relatively consistent shade of green suggesting even chlorophyll distribution.
            - The average mildewed leaf looks to have a blotchy appearance and lighter shade indicating chlorophyll depletion in some areas.
            - The image representing the difference between average images shows a large black centre with purple and green edges.
                       
            This suggests:
                       
            - Minimal to no differences between average healthy and average mildewed leaves at the centre.
            - Greater variation between avergae healthy and average mildewed leaves at the edges.
                       
            """)

            if avg_diff_path.exists():
                difference_between = plt.imread(str(avg_diff_path))
                diff_caption = 'The Difference Between the Average Images'
                st.image(difference_between, caption=diff_caption)
            else:
                st.warning(
                    "⚠️ Image file not found. Please check your file path.")
                
            st.write("---")

        # Checkbox: Image Montage
        if st.checkbox("Image montage"): 
            st.header("🔍 Image Montage", divider=True)
            st.success("Here you can see a montage of healthy and mildewed cherry leaves.\n"
            "Choose your category and hit '🔄 Refresh Montage' to see more images.")
            st.subheader("🤔 Choose image type:", divider=True)
            selection = st.radio("Select leaf type", [
                "Healthy", "Powdery Mildew"], horizontal=True, 
                label_visibility="hidden")
            # Call the image montage function
            image_montage(selection)


    # Call the visualization function
    data_visual_body()