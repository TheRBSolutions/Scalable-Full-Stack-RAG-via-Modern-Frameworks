---
id: humanoid
title: Humanoid Robotics Basics
---

Humanoid robots are designed to mimic the human form, primarily to navigate environments built for humans (stairs, doorways, tools). This chapter covers the structural design and bipedal philosophy of modern humanoids like Tesla Optimus, Figure 01, and Boston Dynamics Atlas.

### Structural Design
Humanoids generally consist of a torso, two arms, two legs, and a head. Each of these components requires specific degrees of freedom (DoF). A human-like arm typically requires at least 7 DoF to reach any point in space with any orientation.

### Challenges of Bipedalism
Walking on two legs is essentially a continuous process of "controlled falling." We will examine:
* **Center of Mass (CoM):** Keeping the weight centered over the support polygon.
* **Zero Moment Point (ZMP):** A key concept in balancing algorithms.
* **Actuators:** The "muscles" of the robot, often utilizing high-torque density electric motors or hydraulic systems.