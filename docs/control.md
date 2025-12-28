---
id: control
title: Control Systems
---

Control systems are the "brain-to-muscle" connection. They translate high-level goals into specific electrical signals for the motors.

### Classical Control (PID)
Proportional-Integral-Derivative (PID) control is the most common algorithm. It calculates the error between the desired position and the actual position, then applies a correction force.

### Advanced Control: MPC
Model Predictive Control (MPC) looks into the future. It uses a mathematical model of the robot to predict how it will move over the next few seconds and optimizes the "best" path in real-time.

### Reinforcement Learning (RL)
Modern Physical AI often uses RL, where a robot learns to walk or grasp objects through millions of trials in a simulator (NVIDIA Isaac Gym) before being deployed to the real world.