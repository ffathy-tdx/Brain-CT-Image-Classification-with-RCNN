[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/H5WNMtcT)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12729090&assignment_repo_type=AssignmentRepo)

# Brain CT Image Classification with RCNN

## Overview

This project focuses on the classification of Brain CT images into two categories: "Hemorrhage" and "Normal" using a Recurrent Convolutional Neural Network (RCNN) architecture. The primary goal is to develop a robust model capable of accurately identifying potential hemorrhages in medical imaging.
This project aims to classify medical images into different categories using a Convolutional Neural Network (CNN) with Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) layers. The combination of these layers allows the model to capture spatial and temporal information, making it suitable for medical image analysis tasks.


## Key Features

- Utilizes a combination of Convolutional Neural Network (CNN) and Recurrent Neural Network (RNN) layers for sequential data processing.
- Implements image data augmentation techniques to enhance model generalization and reduce overfitting.
- Provides visualizations of dataset distributions, training metrics, and sample predictions.
- Incorporates early stopping callbacks to prevent overfitting and improve training efficiency.
- Offers flexibility for customization and further experimentation with model parameters.

## Usage

1. **Install Dependencies:**

   ```bash
   pip install pandas numpy seaborn matplotlib tensorflow keras scikit-learn
   
The dataset comprises Brain CT images with corresponding labels indicating either "Hemorrhage" or "Normal" conditions. The dataset is not provided in this repository, but users can substitute it with their own medical imaging dataset.

Structure

main_script.py: The main script containing the code for data preprocessing, model construction, training, and evaluation.

data/: Placeholder for the dataset directory. Users need to organize their dataset in this directory with appropriate subfolders.

results/: Placeholder for storing model training visualizations and evaluation metrics.

Results

The model's performance metrics, including accuracy and loss, are visualized during and after the training process. Sample predictions with corresponding images are also displayed.
