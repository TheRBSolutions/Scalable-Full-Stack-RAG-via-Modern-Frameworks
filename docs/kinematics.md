---
id: kinematics
title: Kinematics & Movement
---

Kinematics is the study of motion without considering the forces that cause it. In robotics, we focus on two primary types: **Forward Kinematics (FK)** and **Inverse Kinematics (IK)**.

### Forward Kinematics
If you know the angles of every joint in a robot arm, FK allows you to calculate exactly where the hand (end-effector) is in 3D space. This is usually handled using Denavit-Hartenberg (DH) parameters.

### Inverse Kinematics
This is the harder, more important problem: If you want the robot's hand to pick up a coffee mug at $(x, y, z)$, what should the joint angles be?
$$
\theta = f^{-1}(x, y, z)
$$
Because there are often multiple ways to reach the same point, IK requires sophisticated solvers to choose the most efficient or safest movement path.