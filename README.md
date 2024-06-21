# YOLO Object Detection Streamlit App

## Overview

The YOLO Object Detection Streamlit App is an innovative web application that identifies and lists objects within any uploaded image. Utilizing advanced machine learning algorithms and built with the powerful Streamlit framework, this tool offers users an easy and intuitive way to explore the contents of their photos. Whether for personal curiosity, educational purposes, or professional analysis, the application provides accurate and immediate object detection results. Upload an image, and let the technology unveil all the hidden details for you!

## Features

- **Easy Image Upload:** Drag and drop your images or browse your files to upload.
- **Accurate Object Detection:** Utilizes the YOLO (You Only Look Once) algorithm for precise and quick object detection.
- **Real-Time Results:** Get immediate feedback with a list of detected objects and their locations within the image.
- **User-Friendly Interface:** Built with Streamlit, offering a clean and intuitive user experience.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- ImageAI (v3.0.3)

### Model Download

Due to its large size a couldn't push it to the resp so you can download **YOLOv3** from official [ImageAi GitHub repo]([GitHub - OlafenwaMoses/ImageAI: A python library built to empower developers to build applications and systems with self-contained Computer Vision capabilities](https://github.com/OlafenwaMoses/ImageAI/tree/master)) and put it inside a folder with name <mark>models</mark>.

## Usage

1. Run the Streamlit app:
   
   ```sh
   streamlit run main.py
   ```

2. Open your browser and navigate to `http://localhost:8501` to use the app.

## Project Structure

```
yolo-object-detection-streamlit-app/
│
├── main.py             # Main application file
├── models/             # Directory for storing YOLO models
├── tempSaves/          # Temporary saving files
├── result-extracted/   # Object extraction images
└── README.md           # Project documentation
```