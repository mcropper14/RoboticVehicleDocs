# RoboticVehicleDocs

Documentation for ROS (Robot Operating System) Vehicles.

This repository provides documentation and example scripts to assist with ROS-based robotic vehicle operations. Please ensure you are using Docker to access and run the provided robot scripts.

## Requirements
- Docker: All scripts and tools must be run within a Docker container. Use the provided `run_docker.sh` script to set up and enter the container.

## Quick Start

1. Clone this repository.
2. Run Docker with:
   ```bash
   ./run_docker.sh

RoboticVehicleDocs/
├── ExampleCode/
│   ├── basic_robot_lidar.py          # Basic LIDAR functionality
│   ├── basic_robot_movement.py       # Basic movement functions
│   └── open_camera.py                # Script to open and use the camera
├── Instructions/
│   └── install_vscode.txt            # Instructions to install VS Code
├── Troubleshooting/
│   ├── camera_not_working.txt        # Help for camera issues
│   ├── docker_help.txt               # General Docker troubleshooting tips
│   ├── docker_issues.txt             # Common Docker issues and solutions
│   ├── start_nodes.txt               # Instructions to start nodes in ROS
│   └── vnc_commands.txt              # VNC commands for remote access
├── README.md                         # Project documentation (this file)
└── run_docker.sh    