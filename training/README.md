# YOLOv8 Object Detection Training

## Overview
This repository contains the necessary files for training object detection models using YOLOv8. It includes support for multi-GPU training, various YOLOv8 model sizes (nano, small, medium, large, xlarge).

## Requirements
To run the training scripts, you need to install the dependencies listed in `requirements.txt`. This includes various Python libraries like PyTorch, Comet ML for experiment tracking, and utilities for monitoring system resources.

### Installation
To install the requirements, use the following command:
`pip install -r requirements.txt`


## Configuration of Tracking Training Process (optional)
Before starting the training, ensure that the environment variable `COMET_EVAL_LOG_CONFUSION_MATRIX` is set. This can be done by running:

`export COMET_EVAL_LOG_CONFUSION_MATRIX=true`



## Running the Training Script
The main training script is `train.py`. This script will use GPUs for training. It will load the selected YOLOv8 model and perform training based on the hyperparameters specified in `hyperparameters.json`.

### Executing the Script
Run the script using the following command:

`python train.py`


### Logging
Training logs are saved to `training_log.log`. This includes information about the model being trained, system resource usage, and training progress.

## Models
Several YOLOv8 models are available, with paths specified in the training script. You can choose which model to load by setting the `load` flag to `True` for the desired model in the `models_to_load` dictionary.

## Hyperparameters
Training hyperparameters are specified in `hyperparameters.json`. Adjust these parameters as needed to fit your training requirements.

