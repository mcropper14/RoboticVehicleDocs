cd into source, or create your own directory 
``` mkdir directory_name ```
or to place the node in the existing structure 
``` cd ~/yahboom_ros2_ws/yahboomcar_ws/src ```

Create the node:
``` ros2 pkg create package_name --build-type ament_python --depencies rclpy --node-name node_name ```

This creates a package named package_name and a node_name.py file 

To compile the package run: ``` colcon build --packages-select package_name ```
``` source install/setup.bach ```

Run the node: ``` ros2 run package_name node_name ```

