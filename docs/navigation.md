---
id: navigation.md
title: Autonomous Navigation
---

Navigation is the ability of a robot to move from Point A to Point B without human intervention. This requires solving two simultaneous problems: "Where am I?" and "How do I get there?"

### SLAM (Simultaneous Localization and Mapping)
SLAM is the process where a robot builds a map of an unknown environment while keeping track of its own location within that map.

### Path Planning
* **Global Planning:** Finding the overall route through a building.
* **Local Planning:** Making split-second decisions to step over a cable or avoid a person walking by.
* **Obstacle Avoidance:** Using "Costmaps" to identify areas that are unsafe for the robot to occupy.