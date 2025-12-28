---
id: control
title: Control Systems
---

# Control Systems: The Brain-Body Connection

Control theory is what allows a robot to translate a plan into physical reality. It is the math that governs how much current is sent to a motor to achieve a desired motion while resisting external disturbances like wind or a push.

## 1. PID Control: The Bedrock
The Proportional-Integral-Derivative (PID) controller is the most widely used algorithm in history.
* **Proportional:** Corrects the error based on how far the robot is from the goal.
* **Integral:** Corrects based on how long the robot has been stuck.
* **Derivative:** Predicts future error to slow the robot down before it overshoots.
While great for simple arms, PID is often too "dumb" for a 50-joint humanoid.

## 2. Model Predictive Control (MPC)
MPC is the modern standard for humanoid balance. Instead of just reacting to the current error (like PID), MPC uses a physics model of the robot to **predict the future**. 
It asks: "If I apply $X$ force now, where will my foot be in 0.5 seconds?" It solves a massive optimization problem 500 times per second to ensure the robot stays upright even on uneven terrain.



## 3. Impedance and Force Control
Old industrial robots were "Position Controlled"—they would move to a coordinate regardless of what was in the way. Modern Physical AI uses **Impedance Control**. This makes the robot "compliant" or "soft." If you push a robot's arm, it yields to your touch. This is essential for "Human-Robot Collaboration," ensuring the robot doesn't crush a human hand if a collision occurs.

## 4. Reinforcement Learning (RL) in Control
The newest frontier is "Learning-based Control." Instead of engineers writing equations, the robot spends 10,000 hours in a simulation (NVIDIA Isaac) learning to walk by trial and error. The result is a "Neural Network Policy" that can handle complex movements, like a backflip or running on sand, that are nearly impossible to code by hand.