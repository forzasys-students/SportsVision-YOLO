# YOLOv8 Hyperparameter Tuning Script

## Overview
This script is designed for hyperparameter tuning of the YOLOv8 model for object detection tasks. It utilizes the Ultralytics YOLO framework and Ray Tune for efficient hyperparameter optimization.

## Setting Up
Before running this script, ensure that all necessary libraries are installed, including Ultralytics YOLO and Ray Tune. The script sets the `WANDB_API_KEY` environment variable for Weights & Biases integration, which is essential for experiment tracking.

### Installation
You might need to install the required packages if they are not already present in your environment:

`pip install ultralytics ray[tune]`


### Script Features

Model Loading: The script loads a YOLOv8 model. Make sure to have the model file available or adjust the path in the script accordingly.

Hyperparameter Search Space: A comprehensive search space for YOLOv8 training is defined, covering learning rates, momentum, weight decay, augmentation parameters, and more.

Hyperparameter Tuning: Utilizes Ray Tune for optimizing these parameters.


### Running the Script
To execute the script, simply run it in your Python environment:

`python yolo_hyper_tuning.py`


### Data and Configuration

Data Path: Modify the data path in the `model.tune()` method to point to your dataset configuration file (`config.yaml`).

Training Configuration: The script is set up for multi-GPU training. Adjust the device and `gpu_per_trial` parameters according to your setup.