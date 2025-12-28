---
id: sensors
title: Sensor Integration
---

For a robot to interact with the world, it must first perceive it. Sensor integration is the process of combining data from various inputs to create a cohesive internal model of the environment.

### Primary Sensor Types
* **Vision (RGB-D):** Cameras provide color data, while depth sensors (like Intel RealSense) provide distance data, allowing for 3D reconstruction.
* **LiDAR:** Uses laser pulses to create high-precision point clouds of the surroundings, essential for obstacle avoidance.
* **IMU (Inertial Measurement Unit):** Combines accelerometers and gyroscopes to help the robot maintain balance and understand its orientation.
* **Force/Torque Sensors:** Located at the joints or "fingertips," these allow the robot to feel resistance when picking up objects.

### Sensor Fusion
Sensor fusion is the mathematical process (often using Kalman Filters) of combining noisy data from multiple sensors to get a more accurate estimate of the robot's state than any single sensor could provide.