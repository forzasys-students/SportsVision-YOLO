# SportObjectDetection-YOLOv8

Welcome to the `SportsVision-YOLOv8` repository, where we have fine-tuned the YOLO v8 model for specific sports object detection tasks. Our models are tailored for two popular sports: Soccer and Ice Hockey.

## Models

### Soccer Detection Model
- **Objective**: Detect soccer balls and players.
- **Training Data Description**: The dataset comprises approximately 1300 frames from soccer matches across Eliteserien, Allsvenskan, and Toppserien. It includes various scenarios identified as edge cases in soccer clips. These scenarios range from the ball being airborne, not on the green field, to situations where the ball is closely adhered to the player's foot. Additionally, the dataset encompasses a diversity of colors present in these matches.


##### Link to the Dataset: 
https://drive.google.com/drive/folders/1T4MU8wzKYZ6osIweuieBf1EGrIV3l-lv?usp=drive_link

- **Performance Metrics**: [Include key performance metrics, e.g., accuracy, precision, recall, etc.]
| Metric                     | Detail                            |
|----------------------------|-----------------------------------|
| **Train Scenario**         | 11                                |
| **Project Name**           | senario_11                        |
| **Model Name**             | YOLOV8_sc11                       |
| **Yolo Version**           | YOLOv8m-football                  |
| **Epochs**                 | 200                               |
| **Agnostic NMS**           | TRUE                              |
| **Image Size**             | 1280                              |
| **Batch Size**             | 96                                |
| **Patience**               | 100                               |
| **Optimizer**              | adamW                             |
| **Learning Rate**          | 0.001                             |
| **Drop Out**               | 0.5                               |
| **Model Size**             | 52.1 MB                           |
| **Ball True Positive (TP)**| 82%                               |
| **Ball False Negative (FN)**| 18%                              |
| **Player TP**              | 99%                               |
| **Player FN**              | 1%                                |
| **Logo TP**                | 99%                               |
| **Logo FN**                | 1%                                |
| **PR Player**              | 98%                               |
| **PR Ball**                | 82%                               |
| **PR Logo**                | 98%                               |
| **PR All Classes**         | 92%                               |
| **Execution Time**         | 78 seconds (1250 frames, 4GB GPU) |
| **Inputs**                 | Config parameters + 32s 1280p video at 25fps |
| **Note**                   | Additional details or observations |


### Ice Hockey Detection Model
- **Objective**: Detect ice hockey pucks and players.
- **Training Data Description**: [Brief description of the training data].
- **Performance Metrics**: [Key performance metrics].

## Papers
