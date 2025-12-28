---
id: sensors
title: Sensor Integration
---

# Sensor Integration: Perception in Physical AI

For a robot to be "intelligent," it must be able to perceive its environment. Sensors are the windows through which the Physical AI brain sees, feels, and understands the world.

## 1. Exteroceptive Sensors (Outside World)
* **Vision (RGB-D):** Standard cameras provide color, but "Depth" (D) cameras (like the Intel RealSense) provide a 3D point cloud. This allows the robot to know not just that there is a chair, but exactly how many centimeters away it is.
* **LiDAR (Light Detection and Ranging):** By spinning a laser and measuring the reflection time, LiDAR creates a high-fidelity 360° map. This is the primary sensor for navigation and obstacle avoidance.
* **Tactile Sensing:** Modern humanoids are being wrapped in "Electronic Skins." These allow the robot to feel the difference between a delicate egg and a heavy wrench, adjusting its grip strength accordingly.

## 2. Proprioceptive Sensors (Self-Awareness)
* **IMU (Inertial Measurement Unit):** This is the robot's "inner ear." It uses accelerometers and gyroscopes to detect gravity and orientation. If the IMU detects a sudden tilt, the control system triggers a "recovery step" to prevent a fall.
* **Encoders:** These are located inside every motor. They measure the exact position of the shaft, often down to 0.001 degrees of accuracy.



## 3. The Challenge of Sensor Fusion
No single sensor is perfect. LiDAR is bad at seeing glass; cameras are bad at seeing in the dark. **Sensor Fusion** is the mathematical process of combining data from multiple sources to create a "Single Source of Truth." 
Using **Kalman Filters** or **Factor Graphs**, the robot can decide: "The camera sees a shadow, but the LiDAR sees a solid object—I will trust the LiDAR and stop moving."

## 4. Latency and Data Throughput
Processing 4K video at 60fps alongside high-frequency LiDAR data requires massive onboard compute (like NVIDIA Orin). In Physical AI, the time it takes for a photon to hit the camera and the motor to react is the "Perception-to-Action Latency." If this is higher than 50ms, the robot cannot safely interact with humans.