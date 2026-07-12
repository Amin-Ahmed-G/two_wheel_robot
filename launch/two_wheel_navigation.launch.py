import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch_ros.actions import SetRemap, Node

def generate_launch_description():
    pkg_share = get_package_share_directory('two_wheel_robot')

    # 1. Include the Gazebo simulation launch
    two_wheel_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'two_wheel_gazebo.launch.py')
        )
    )

    # 2. Include the SLAM Toolbox online async launch
    slam_toolbox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('slam_toolbox'),
                         'launch', 'online_async_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'true'
        }.items()
    )

    # 3. Include the Nav2 navigation launch with our custom params file
    nav2_params_file = os.path.join(pkg_share, 'config', 'nav2_params.yaml')
    nav2_navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('nav2_bringup'),
                         'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'params_file': nav2_params_file
        }.items()
    )

    # Group Nav2 launch to apply remappings to its components
    nav2_with_remappings = GroupAction(
        actions=[
            SetRemap(src='cmd_vel', dst='/diff_drive_controller/cmd_vel'),
            SetRemap(src='odom', dst='/diff_drive_controller/odom'),
            SetRemap(src='/odom', dst='/diff_drive_controller/odom'),
            nav2_navigation
        ]
    )

    # 4. Include the Rosbridge WebSocket launch for the web dashboard (XML format)
    rosbridge = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(
            os.path.join(get_package_share_directory('rosbridge_server'),
                         'launch', 'rosbridge_websocket_launch.xml')
        )
    )

    # 5. Node to publish robot pose in map frame based on TF
    tf_to_pose = Node(
        package='two_wheel_robot',
        executable='tf_to_pose_publisher.py',
        output='screen'
    )

    return LaunchDescription([
        two_wheel_gazebo,
        slam_toolbox,
        nav2_with_remappings,
        rosbridge,
        tf_to_pose
    ])
