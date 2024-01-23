# Import necessary libraries

import os
# Set WANDB_API_KEY environment variable
os.environ['WANDB_API_KEY'] = 'e8e33cb006b988f502f4df3f3f91804af8510185'

from ultralytics import YOLO
from ray import tune




# Load a YOLOv8n model
model = YOLO('/home/mehdihou/D1/YOLO-Train/Train/Models/Detection/medium/yolov8m.pt')  # Ensure 'yolov8n.pt' is available in your directory or specify the full path

# Define the search space for hyperparameters
search_space = {
    "lr0": tune.uniform(1e-5, 1e-1),          # Initial learning rate
    "lrf": tune.uniform(0.01, 1.0),           # Final learning rate factor
    "momentum": tune.uniform(0.6, 0.98),      # Momentum
    "weight_decay": tune.uniform(0.0, 0.001), # Weight decay
    "warmup_epochs": tune.uniform(0.0, 5.0),  # Warmup epochs
    "warmup_momentum": tune.uniform(0.0, 0.95),# Warmup momentum
    "box": tune.uniform(0.02, 0.2),           # Box loss weight
    "cls": tune.uniform(0.2, 4.0),            # Class loss weight
    "hsv_h": tune.uniform(0.0, 0.1),          # Hue augmentation range
    "hsv_s": tune.uniform(0.0, 0.9),          # Saturation augmentation range
    "hsv_v": tune.uniform(0.0, 0.9),          # Value (brightness) augmentation range
    "degrees": tune.uniform(0.0, 45.0),       # Rotation augmentation range (degrees)
    "translate": tune.uniform(0.0, 0.9),      # Translation augmentation range
    "scale": tune.uniform(0.0, 0.9),          # Scaling augmentation range
    "shear": tune.uniform(0.0, 10.0),         # Shear augmentation range (degrees)
    "perspective": tune.uniform(0.0, 0.001),  # Perspective augmentation range
    "flipud": tune.uniform(0.0, 1.0),         # Vertical flip augmentation probability
    "fliplr": tune.uniform(0.0, 1.0),         # Horizontal flip augmentation probability
    "mosaic": tune.uniform(0.0, 1.0),         # Mosaic augmentation probability
    "mixup": tune.uniform(0.0, 1.0),          # Mixup augmentation probability
    "copy_paste": tune.uniform(0.0, 1.0),      # Copy-paste augmentation probability
    "cos_lr": tune.choice([True, False]),
    "optimizer": tune.choice(['SGD', 'Adam', 'Adamax', 'AdamW', 'NAdam', 'RAdam', 'RMSProp', 'auto']),
}


# Start tuning hyperparameters for YOLOv8n training on the COCO8 dataset
result_grid = model.tune(data='/home/mehdihou/D1/YOLO-Train/Train/config.yaml', 
                         space=search_space,
                         batch=64,
                         device=[0,1,2,3,4,5,6,7],
                         gpu_per_trial=8,
                         iterations=150,
                         epochs=200,
                         imgsz = 1280,
                         use_ray=True,
                         )