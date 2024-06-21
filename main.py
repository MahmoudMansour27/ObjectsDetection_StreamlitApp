# Streamlit Object Detection App

# import libraries
import streamlit as st
from ObjectDetection_extraction import detect
import os
import shutil


st.title("🔍 What's in Your Photo? Find Out Now!")
st.write("Uncover the contents of your photos with ease! Our image object detection tool allows you to upload any image and instantly identifies and lists all objects within it. Upload now to explore and discover!")
image_path = st.file_uploader("Upload an Image")

# Save uploaded image to local temp files
path = "tempSaves/uploadedImage.jpg"
if image_path: 
    with open(path, "wb") as f:
        f.write(image_path.getvalue())
        

# Detect button function
def detectBtn():
    if  image_path:
        # display input image
        c.image(path, caption= "Input Image")
        
        # delete last extracted images
        if os.path.isdir("result-extracted"):
            shutil.rmtree("result-extracted")
        
        # detection function
        detections = detect(path)
        
        # display input image
        c.image("result.jpg", caption= "Output Image")
        
        # extraction section
        c.header("Extracted Objects 🚀️")
        
        for eachObject, objectPath in detections:
            c.text(f'Name: {eachObject["name"]} \nProbability: {eachObject["percentage_probability"]}')
            c.image(objectPath)
            c.markdown("#####")
    
    
    
    
st.button("Analyse Image 🧐️", on_click = detectBtn)
st.markdown("---")
c = st.container()


# side bar
st.sidebar.header("Reference")
st.sidebar.write("You'll find comprehensive resources and guides on how to make the most of our image object detection tool. Built with Streamlit, our application offers step-by-step tutorials, FAQs, and troubleshooting tips to enhance your experience and help you understand the technology behind object detection. Dive in to learn more and get the best results from your image uploads!")
st.sidebar.subheader("Useful Links:")
st.sidebar.markdown("- [Streamlit Documentation](https://docs.streamlit.io/) \n - [ImageAI (v3.0.3) GitHub](https://github.com/OlafenwaMoses/ImageAI/tree/master)")



