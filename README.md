# 🤖 Two Wheel Robot - ROS 2 Jazzy Differential Drive Simulation

A ROS 2 Jazzy differential drive robot simulation developed using Gazebo. The project demonstrates robot modeling, simulation, and control, forming the foundation for autonomous mobile robotics.

---

## 🚀 Features

- Differential Drive Robot
- ROS 2 Jazzy
- Gazebo Simulation
- RViz Visualization
- URDF/Xacro Robot Model
- Controller Configuration
- LiDAR Ready
- Camera Ready

---

## 📂 Project Structure

```
two_wheel_robot/
├── config/
│   └── two_wheel_controllers.yaml
├── launch/
│   └── two_wheel_gazebo_launch.py
├── src/
│   └── waypoint_follower_node.py
├── urdf/
│   └── 2_wheel.xacro
├── worlds/
│   └── two_wheel_world.sdf
├── CMakeLists.txt
├── package.xml
└── README.md
```

---

## 🛠 Requirements

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Harmonic
- colcon
- Python 3

---

## 📦 Build

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

---

## ▶️ Run Simulation

```bash
ros2 launch two_wheel_robot two_wheel_gazebo_launch.py
```

---

## 🧠 Future Improvements

- SLAM Toolbox
- Nav2 Navigation Stack
- Autonomous Waypoint Navigation
- Camera Object Detection
- LiDAR Obstacle Avoidance
- Path Planning
- AMCL Localization
- MoveIt Integration

---

## 📸 Screenshots

### Simulation Video

<video src="two_wheel_robot.mp4" controls="controls" style="max-width: 100%;">
</video>

### Gazebo Simulation

![Gazebo Simulation](image.png)

### Project Screenshot

![Project Screenshot](Screenshot%20from%202026-07-09%2014-51-50.png)
---

## 🛠 Technologies Used

- ROS 2 Jazzy
- Gazebo
- RViz2
- URDF/Xacro
- Python
- CMake

---

## 📈 Roadmap

- [x] Robot Modeling
- [x] Gazebo Simulation
- [x] ROS 2 Package
- [ ] LiDAR Integration
- [ ] Camera Integration
- [ ] SLAM
- [ ] Navigation2
- [ ] Autonomous Exploration

---

## 👨‍💻 Author

**Amin Ahmed G**

Robotics & Automation Engineer

GitHub: https://github.com/Amin-Ahmed-G

LinkedIn: https://linkedin.com/in/your-linkedin-profile

---

⭐ If you found this project useful, consider giving it a star.
