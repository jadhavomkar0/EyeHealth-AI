import streamlit as st
import random

# Mock Prediction Function
def mock_model_prediction():
    """
    Simulates the behavior of a trained model by randomly selecting a class.
    """
    class_names = [
        'Cataract', 'Diabetic Retinopathy - Mild', 'Diabetic Retinopathy - Moderate',
        'Diabetic Retinopathy - Severe', 'Diabetic Retinopathy - Proliferative', 'Glaucoma',
        'Age-related Macular Degeneration - Early', 'Age-related Macular Degeneration - Intermediate',
        'Age-related Macular Degeneration - Late', 'Hypertensive Retinopathy - Stage 1',
        'Hypertensive Retinopathy - Stage 2', 'Hypertensive Retinopathy - Stage 3',
        'Hypertensive Retinopathy - Stage 4', 'Retinal Vein Occlusion', 'Retinal Artery Occlusion',
        'Macular Edema', 'Normal', 'Pathological Myopia', 'Optic Neuritis', 'Central Serous Retinopathy'
    ]
    return random.choice(class_names)  # Randomly select a class for demonstration

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Detection"])

# Main Page
if app_mode == "Home":
    st.header("EYE HEALTH AI SYSTEM")
    st.image("Designer.png", use_column_width=True)  # Replace with your banner image
    st.markdown("""
    Welcome to the **Eye Health AI System**! 👁️🔍
    
    Our goal is to assist in the early detection of retinal diseases. By leveraging advanced AI techniques, we aim to ensure better eye health outcomes for everyone.

    ### Features
    1. **Upload Images:** Use the **Disease Detection** page to upload fundus images.
    2. **AI Analysis:** Simulates how the AI model analyzes the images.
    3. **Diagnosis:** Mock predictions for demonstrating system flow.

    ### Supported Diseases
    - Cataract
    - Diabetic Retinopathy
    - Glaucoma
    - Other conditions classified in 20 categories

    ### Get Started
    Use the **Disease Detection** page to upload an image and explore the UI.
    """)

elif app_mode == "About":
    st.header("About the Project")
    st.markdown("""
    #### Dataset Overview
    This project aims to utilize a curated dataset of retinal images for multi-class classification of common eye diseases. The dataset will include:
    - Training Images: Preprocessed and augmented for better model generalization.
    - Validation Images: Used to tune the model performance.
    - Test Images: Held-out images for final evaluation.

    #### Future Features
    - Pretrained CNN models such as ResNet50, VGG-16, Xception, and EfficientNetB7.
    - Ensemble stacking for improved accuracy.
    - Focus on early disease detection for better patient outcomes.

    #### Goal
    To create an accessible, AI-powered solution for eye health professionals and individuals to screen for retinal diseases efficiently.
    """)

elif app_mode == "Disease Detection":
    st.header("Disease Detection")
    test_image = st.file_uploader("Upload a Retinal Fundus Image:", type=["jpg", "png", "jpeg"])
    
    if test_image is not None:
        if st.button("Show Image"):
            st.image(test_image, use_column_width=True, caption="Uploaded Image")
        
        # Predict Button
        if st.button("Predict"):
            st.write("Analyzing the image...")
            # Mock Prediction
            result = mock_model_prediction()
            st.success(f"The system predicts: **{result}**")
