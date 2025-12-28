import os

chapters = {
    "intro.md": ("Introduction to Physical AI", "The convergence of LLMs and robotics..."),
    "humanoid.md": ("Humanoid Robotics Basics", "Structural design and bipedal philosophy..."),
    "kinematics.md": ("Kinematics & Movement", "Forward and inverse kinematics for actuators..."),
    "sensors.md": ("Sensor Integration", "Lidar, Depth cameras, and Proprioception..."),
    "control.md": ("Control Systems", "PID, MPC, and Reinforcement Learning..."),
    "navigation.md": ("Autonomous Navigation", "SLAM and path planning in dynamic environments..."),
    "applications.md": ("Real-world Applications", "Industrial automation and domestic service...")
}

for filename, (title, summary) in chapters.items():
    with open(f"docs/{filename}", "w") as f:
        f.write(f"---\nid: {filename.replace('.md', '')}\ntitle: {title}\n---\n\n")
        f.write(f"# {title}\n\n{summary}\n\n" + ("Textbook content goes here... " * 100)) # Placeholder for your AI generation
    print(f"Created {filename}")

