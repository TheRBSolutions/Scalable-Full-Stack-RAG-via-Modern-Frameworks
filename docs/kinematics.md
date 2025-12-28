---
id: kinematics
title: Kinematics & Movement
---

# Kinematics: The Mathematics of Robotic Motion

Kinematics is the branch of mechanics that describes the motion of points, bodies, and systems of bodies without considering the forces that cause the motion. In robotics, it is the bridge between a software command (e.g., "pick up that tool") and the mechanical reality of joint rotation.

## 1. Forward Kinematics (FK)
Forward Kinematics is the process of calculating the position and orientation of the "End-Effector" (the hand or tool) based on the known joint angles. 
Imagine a 3-link arm. If Joint 1 is at 30°, Joint 2 at 45°, and Joint 3 at 10°, where is the fingertip? 
We solve this using **Homogeneous Transformation Matrices**. Each joint is assigned a coordinate frame, and we multiply these matrices ($T_1 \times T_2 \times T_3$) to map the position from the base of the robot to the tip of the hand.

## 2. Inverse Kinematics (IK)
Inverse Kinematics is the "Hard Problem." It asks: "If I want my hand to be at coordinates $(x, y, z)$, what angles should my joints be at?"
This is complex because:
* **Multiple Solutions:** You can touch your ear with your elbow pointed down or your elbow pointed up. The robot must decide which path is safer or uses less energy.
* **Singularities:** Mathematical points where the robot loses a degree of freedom. For example, when an arm is fully extended, it cannot move "further" out, causing the math to "divide by zero" and the robot to lock up.



## 3. The Denavit-Hartenberg (DH) Convention
To keep track of all these frames in a 50-DoF humanoid, roboticists use the DH Convention. It reduces the relationship between two joints to four simple parameters:
1. **Link Length ($a$):** Distance between axes.
2. **Link Twist ($\alpha$):** Angle between axes.
3. **Link Offset ($d$):** Distance along the axis.
4. **Joint Angle ($\theta$):** The rotation provided by the motor.

## 4. Jacobian Matrices and Velocity
Kinematics isn't just about *where* the robot is, but how *fast* it is moving. The **Jacobian Matrix** relates joint velocities to end-effector velocities. This is crucial for smooth motion; without a properly calculated Jacobian, the robot’s movements would be jerky, leading to mechanical wear and safety risks.