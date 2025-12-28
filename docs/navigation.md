---
id: navigation
title: Path Planning
---

# Autonomous Navigation: SLAM and Path Planning

Navigation is the ability of a robot to move from Point A to Point B autonomously. This is not just about moving forward; it is about mapping, localization, and dynamic obstacle avoidance.

## 1. The Mapping Problem: SLAM
**Simultaneous Localization and Mapping (SLAM)** is the "chicken and egg" problem of robotics. To build a map, the robot needs to know where it is. To know where it is, it needs a map. 
SLAM algorithms (like Cartographer or ORB-SLAM) solve this by finding "landmarks"—the corner of a table, a distinct floor pattern—and tracking them over time to triangulate the robot's position while simultaneously drawing the walls on a digital grid.

## 2. Global vs. Local Planning
* **Global Planner:** This looks at the big picture. "I am in the kitchen; I need to go to the front door." It uses algorithms like **A* (A-Star)** to find the shortest path on a 2D map.
* **Local Planner:** This is the "reactive" layer. It looks 2 meters in front of the robot. If a cat runs across the path, the local planner immediately deviates from the global path to avoid a collision, recalculating the trajectory in milliseconds.



## 3. Costmaps and Navigation Grids
Robots see the world through "Costmaps." 
* **Zero Cost:** Clear floor.
* **High Cost:** Near a wall (risky).
* **Infinite Cost:** A solid obstacle or a "No-Go Zone."
The robot’s navigation system always searches for the path of "Least Cost."

## 4. Semantic Navigation
The future of navigation is "Semantic." Instead of telling a robot to go to coordinates $(x=5.2, y=10.1)$, we use Physical AI to say "Go to the kitchen." The robot must recognize what a "kitchen" looks like, understand the context, and navigate there without a pre-loaded map.