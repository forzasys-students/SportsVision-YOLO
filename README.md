# SportsVision-YOLO

Welcome to the `SportsVision-YOLO` repository, where we have fine-tuned the YOLO v8 model for specific sports object detection tasks. Our models are tailored for two popular sports: Soccer and Ice Hockey.

## Models

### Soccer Detection Model
- **Objective**: The primary goal of the project is to detect Balls, Players, and Logos on the soccer pitch across various types of camera shots, ranging from wide-angle views to close-up shots. This comprehensive detection aims to accurately identify these key elements in diverse and dynamic soccer match environments.

- **Training Data Description**: The dataset comprises approximately 1300 frames from soccer matches across Eliteserien, Allsvenskan, and Toppserien. It includes various scenarios identified as edge cases in soccer clips. These scenarios range from the ball being airborne, not on the green field, to situations where the ball is closely adhered to the player's foot. Additionally, the dataset encompasses a diversity of colors present in these matches.


- **Training:** 

| Training parameters              | Detail                                      |
|----------------------------------|---------------------------------------------|
| **Yolo Version**                 | YOLOv8 - Medium                             |
| **Epochs**                       | 200                                         |
| **Agnostic NMS**                 | TRUE                                        |
| **Image Size**                   | 1280                                        |
| **Batch Size**                   | 96                                          |
| **Patience**                     | 100                                         |
| **Optimizer**                    | adamW                                       |
| **Learning Rate**                | 0.001                                       |
| **Drop Out**                     | 0.5                                         |
| **Model Size**                   | 52.1 MB                                     |

- **Performance:** 

| Metric                           | Detail                                      |
|----------------------------------|---------------------------------------------|
| **Ball True Positive (TP)**      | 82%                                         |
| **Ball False Negative (FN)**     | 18%                                         |
| **Player TP**                    | 99%                                         |
| **Player FN**                    | 1%                                          |
| **Logo TP**                      | 99%                                         |
| **Logo FN**                      | 1%                                          |
| **Precision Recall (PR) Player** | 98%                                         |
| **Precision Recall (PR) Ball**   | 82%                                         |
| **Precision Recall (PR) Logo**   | 98%                                         |
| **Precision Recall (PR) All Classes** | 92%                                  |

- **Execution:** 

| Model Execution                  | Detail                                      |
|----------------------------------|---------------------------------------------|
| **Execution Time**               | 78 seconds (4GB GPU)           |
| **Inputs**                       | 32s 1280p video at 25fps |

##### Link to the trainig sheet:
https://docs.google.com/spreadsheets/d/1MXJZbh9JmHIsDejrBAAIB73V_QeDird1ET3RopYXqP4/edit?usp=sharing




### Ice Hockey Detection Model
- **Objective**: Detect ice hockey pucks and players.
- **Training Data Description**: [Brief description of the training data].
- **Performance Metrics**: [Key performance metrics].

## Papers
