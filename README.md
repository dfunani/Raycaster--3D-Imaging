<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dfunani/RenderEngine--2D-Imaging">
    <img src="public/2DLogo.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Render Engine - 2D Imaging</h3>

  <p align="center">
    Effortless 2D Rendering: Simplifying Image Creation and Visualization
    <br />
    <a href="https://github.com/dfunani/RenderEngine--2D-Imaging"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dfunani/RenderEngine--2D-Imaging">View Demo</a>
    ·
    <a href="https://github.com/dfunani/RenderEngine--2D-Imaging/issues">Report Bug</a>
    ·
    <a href="https://github.com/dfunani/RenderEngine--2D-Imaging/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
<br></br>

## About The Project

The 2D Imaging Render Engine is an open-source initiative, designed to provide a comprehensive yet beginner-friendly platform for rendering 2D images. Tailored for both novices and seasoned contributors, this project offers an intuitive environment to explore, experiment, and contribute to the world of image rendering.

**Objective**

The primary objective of this project is to offer an accessible framework where individuals, regardless of their expertise, can engage in image rendering. Through an adaptable and versatile architecture, the engine encourages experimentation, learning, and collaboration in the realm of 2D image generation.

**Vision**

Our vision is to foster a supportive community that nurtures creativity, innovation, and exploration within the domain of image rendering. We aim to inspire a diverse group of contributors, ranging from beginners to experts, to harness their skills and ideas to enrich the project continually.

**Key Components**

- Rendering Engine Core: The heart of the project, equipped with essential functionalities and algorithms for image generation.
- Comprehensive Documentation: A well-documented guide that assists both newcomers and experienced individuals in understanding the engine's architecture, functions, and APIs.
- Extensive Examples: A collection of illustrative examples, showcasing various rendering techniques and possibilities.
- Contributor-Friendly Environment: A welcoming space that encourages contributions, suggestions, and discussions, fostering a vibrant and inclusive community.

**Image Rendering Basics**

The rendering engine employs various concepts:
- Ray Tracing: Utilizes rays to simulate the way light interacts with objects in a scene.
- Vector Mathematics: Employs vector calculations for geometric operations and transformations.
- Sphere Intersections: Determines intersections between rays and sphere objects within a scene.
- Pixel Generation: Translates traced rays into pixel color values, forming the final image.

**Gallery**

Here are some stunning images rendered using our engine:

<img src="public/sample_output.jpg"/>
<br></br>

Standard output ```./app.py```

<img src="public/test_renderer.jpg"/>
<br></br>

Standard output ```./test_ray_tracer.py```

For more comprehensive details about the project, check [PROJECT_DETAILS.md](./PROJECT_DETAILS.md).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- Python 3.10

**Mac OS**

```zsh
# Homebrew (recommended)
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install Python: brew install python
```

**Windows**

```sh
# Chocolatey (command-line package manager):
# Install Chocolatey
Run: choco install python
```

**Linux (Ubuntu/Debian)**


```sh
sudo apt update
sudo apt install python3

# Alternative Install:

# If Python is not pre-installed, use apt-get or the package manager available for your Linux distribution to install Python.
# For other Linux distributions, you can generally use the package manager (yum, dnf, etc.) to install Python. Refer to your distro's documentation for specific instructions.

```

Always verify the installation by running python --version or python3 --version in the terminal/command prompt to confirm that Python has been successfully installed.

```sh
python --version
```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   # ssh
   git clone git@github.com:dfunani/RenderEngine--2D-Imaging.git
   
   # https
   https://github.com/dfunani/RenderEngine--2D-Imaging.git
   ```
3. Install NPM packages
   ```sh
   pip install -r requirements.txt

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

**Run the Application**

```bash
# This command will launch the render engine and generate the image based on the provided sphere configurations in the app.py file.
python app.py
```

**Modifying Sphere Configurations**

To modify the spheres or their positions:
- Open the app.py file in a text editor.
- Locate the section where spheres are defined.
- Adjust sphere parameters such as center coordinates, radius, material properties, and any other attributes as needed.
- Save the changes to app.py.

**Rendering Custom Scenes**

- By modifying the app.py file, you can create complex scenes by adding, removing, or adjusting sphere parameters to generate different images.

_Ensure that Python is installed on your system before running the application. For Python installation instructions, refer to the "Installing Python" section in the README file._

_Note: Any changes made to the app.py file will reflect in the rendered output when the application is executed._
_Note: All output images will be PPM image format._

## Sample Output

<img src="./public/sample_output.jpg"/>
<br></br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Delali Funani

Project Link: [https://github.com/dfunani/RenderEngine--2D-Imaging](https://github.com/dfunani/RenderEngine--2D-Imaging)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

- [Introduction to Ray-Tracing](https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-ray-tracing/how-does-it-work.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/dfunani/RenderEngine--2D-Imaging/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/dfunani/RenderEngine--2D-Imaging/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/dfunani/RenderEngine--2D-Imaging/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/dfunani/RenderEngine--2D-Imaging/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/dfunani/RenderEngine--2D-Imaging/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/pypi/pyversions/python
[Python-url]: https://python.org/
