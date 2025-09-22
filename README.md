# Satellite Image Classification

## Overview

This project focuses on classifying satellite images into various categories using deep learning techniques. The model is trained on a dataset of satellite images and deployed as a web application for real-time inference.

## Project Structure

.
├── app1.py # Streamlit application for model inference
├── static_cnn_colab_final.keras # Pre-trained model file
├── Task.ipynb # Jupyter notebook for model training and evaluation
├── archive (2).zip # Dataset archive
└── LICENSE # Project license

vbnet
Copy code

## Dataset

The dataset used for training is a collection of satellite images, which can be found in the `archive (2).zip` file. Extract this archive to access the images for training and evaluation.

## Model Training

The model is trained using a Convolutional Neural Network (CNN) architecture. The training process involves:

- Data preprocessing and augmentation
- Model architecture definition
- Compilation and training
- Evaluation on validation data

The training process is documented in the `Task.ipynb` Jupyter notebook.

## Deployment

The trained model is deployed as a web application using Streamlit. The application allows users to upload satellite images and receive predictions on the image's category.

To run the application locally:

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run app1.py
License
This project is licensed under the MIT License - see the LICENSE file for details.

pgsql
Copy code

Feel free to modify this template to better fit your project's specifics.
::contentReference[oaicite:0]{index=0}
