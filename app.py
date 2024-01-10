"""App.py
Responsible for creating the scene. 
By placing Spheres on the Image plane,
using Vector3 and RGB components,
various image scenes can be exported to file.
"""

from typing import Union
from models.vectors import RGB, Vector3
from models.objects import Sphere
from engines.ray_tracer import RayTracer
from utils.types.interfaces import ResponseType
from json import dumps

# // In the main function, we will create the scene which is composed of 5 spheres
# // and 1 light (which is also a sphere). Then, once the scene description is complete
# // we render that scene, by calling the render() function.
def main() -> None:
    """Project Entry Point for creating an Image Scene

    Returns:
        ResponseType: Success or Error depending on runtime
    """
    spheres: list[spheres] = []

    try:
        # Spheres
        spheres.append(
            Sphere(Vector3(0.0, -10004, -20), 10000, RGB(0.20, 0.20, 0.20), 0, 0.0)
        )
        spheres.append(Sphere(Vector3(0.0, 0, -20), 4, RGB(1.00, 0.32, 0.36), 1, 0.5))
        spheres.append(Sphere(Vector3(5.0, -1, -15), 2, RGB(0.90, 0.76, 0.46), 1, 0.0))
        spheres.append(Sphere(Vector3(5.0, 0, -25), 3, RGB(0.65, 0.77, 0.97), 1, 0.0))
        spheres.append(Sphere(Vector3(-5.5, 0, -15), 3, RGB(0.90, 0.90, 0.90), 1, 0.0))
    except BaseException as error:
        response = ResponseType.error
        response.value["message"] = "Couldn't create spheres"
        response.value["error"] = str(error)
        return response

    # light
    try:
        spheres.append(
            Sphere(Vector3(0.0, 20, -30), 3, RGB(0.00, 0.00, 0.00), 0, 0.0, RGB(3, 3, 3))
        )
    except BaseException as e:
        response = ResponseType.error
        response.value["message"] = "Couldn't create lights"
        response.value["error"] = str(error)
        return response
    
    # Scene Renderer/Exporter
    try:
        RayTracer.renderer(spheres, "sample_file")
    except BaseException as e:
        response = ResponseType.error
        response.value["message"] = "Couldn't render scene"
        response.value["error"] = str(error)
        return response
    
    response = ResponseType.success
    response.value["message"] = "Image Successfully exported"
    return response


if __name__ == "__main__":
    result = main()
    print(dumps(result.value, indent=4))
