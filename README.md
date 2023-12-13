
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url] -->
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->

# HoloLens2-ROS2 Interactions ROS Package and XR App
Control your ROS2 Robot using interaction techniques via the HoloLens. This repository contains the ROS2 Node developed for the Novel Human-Robot Interfaces with XR project, as well as a child repository of the [Unity App](https://github.com/septianrazi/HoloLens2-ROS2-Interactions-Unity).

Thinking of using this for your future projects? Feel free to fork it and send a pull request.


<!-- PROJECT LOGO -->
<!-- <br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MRTK Custom Gestures in Unity</h3>

  <p align="center">
    Custom Gestures with Mixed Reality Toolkit!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/septianrazi/MRTK-Custom-Gestures-Unity">View Demo</a>
    ·
    <a href="https://github.com/septianrazi/MRTK-Custom-Gestures-Unity/issues">Report Bug</a>
    ·
    <a href="https://github.com/septianrazi/MRTK-Custom-Gestures-Unity/issues">Request Feature</a>
  </p>
</p> -->



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <!-- <li><a href="#use-in-your-own-projects">Use in your own Projects</a></li> -->
        <li><a href="#running-the-project">Running this Project</a></li>
      </ul>
    </li>
    <li><a href="#examples">Examples</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This code contains the necessary ROS2 node and Flask Python API server.
This project is part of my final project for the Robotics and XR course of University of Eastern Finland in 2023.

See the project in action [on YouTube](https://youtu.be/I6QHjA7SUR8?si%253Dj0qudsOrJZQkcJA3)

### ROS2 Node with Twist commands
Our ROS2 node sends Twist commands to the robot to induce movement. These twist commands can be used with robots generally supporting navigation methods.

### Flask API Server
Our ROS2 node also contains code that allows the Ubuntu Machine where the ROS2 node is being run to act as a server to receive API calls. There are five main endpoints in the code currently, namely */move_forward*,*/move_backwards*, */turn_left*, */turn_right*, and */stop*. When these endpoints are triggered, they will send the appropriate movement to the 

### Built With

* [Python 3.11.4](https://www.python.org/)
* [Flask 3.0.0](https://flask.palletsprojects.com/en/3.0.x/)
* [ROS2 Humble](https://docs.ros.org/en/humble/index.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Ubuntu](https://ubuntu.com/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You will need to download and install the following:
* [ROS2](https://docs.ros.org/en/humble/Installation.html)
* [Docker for Ubuntu](https://docs.docker.com/engine/install/)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/3.0.x/)


### Running the Project

1. Clone the repo
2. Setup ROS2 for ubuntu and connect to the robot (eg [Turtlebot setup](https://turtlebot.github.io/turtlebot4-user-manual/setup/basic.html))
3. Open command line interface and run the following code for first time initialisations:
    ```
    source /opt/ros/humble/setup.bash
    cd ~/hl2_ros2/src
    ros2 pkg create --build-type ament_python --node-name simple_remote_nav hl2_ros2
    ```
4. Once package creation is succesful, we can build with the following commands:
    ```
    cd ~/hl2-ros2/src
    source /opt/ros/humble/setup.bash
    cd ..
    colcon build --symlink-install --packages-select hl2_ros2
    source install/local_setup.bash
    ```
5. Run the package
    ```
    ros2 run hl2_ros2 simple_remote_nav
    ```
6. Open the XR Application either on Unity or on a VAM/XR headset (See [App README.md](HoloLens2-ROS2-Interactions-Unity))
7. Ensure firewall settings are compatible for API calls to be received (is network set to private?)
8. Send commands in the app

## Examples
See the project in action [on YouTube](https://youtu.be/I6QHjA7SUR8?si%253Dj0qudsOrJZQkcJA3)

<!-- CONTRIBUTING -->
## Contributing

If you plan on using this repository for future Robotics and XR project, feel free to fork this project. Once complete, I am more than happy to merge it into this repo as an addition. 
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**. 

1. Choose an Issue you want to work on and assign yourself

   If there is no exsiting issue, please submit one 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request linking the issue


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Septian Razi - [septianrazi.github.io](septianrazi.github.io) - raziseptian@gmail.com

Project Link: [https://github.com/septianrazi/HoloLens2-ROS2-Interactions](https://github.com/septianrazi/HoloLens2-ROS2-Interactions)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [OthNeilDrew's README Template](https://github.com/othneildrew/Best-README-Template)
* [University of Eastern Finland Robotics and AI group](https://sites.uef.fi/edtech/research-labs-and-focus-groups/robotics-and-ai/)

<!-- 
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com) -->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png