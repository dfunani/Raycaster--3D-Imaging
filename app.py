from typing import Union
from models.vectors import RGB, Vector3
from models.objects import Sphere
from engines.ray_tracer import RayTracer

# // In the main function, we will create the scene which is composed of 5 spheres
# // and 1 light (which is also a sphere). Then, once the scene description is complete
# // we render that scene, by calling the render() function.
def main() -> Union[list, None]:
    spheres: list[spheres] = []

    # Spheres
    spheres.append(Sphere(Vector3( 0.0, -10004, -20), 10000, RGB(0.20, 0.20, 0.20), 0, 0.0))
    spheres.append(Sphere(Vector3( 0.0,      0, -20),     4, RGB(1.00, 0.32, 0.36), 1, 0.5))
    spheres.append(Sphere(Vector3( 5.0,     -1, -15),     2, RGB(0.90, 0.76, 0.46), 1, 0.0))
    spheres.append(Sphere(Vector3( 5.0,      0, -25),     3, RGB(0.65, 0.77, 0.97), 1, 0.0))
    spheres.append(Sphere(Vector3(-5.5,      0, -15),     3, RGB(0.90, 0.90, 0.90), 1, 0.0))
    
    # light
    spheres.append(Sphere(Vector3( 0.0,     20, -30),     3, RGB(0.00, 0.00, 0.00), 0, 0.0, RGB(3)))
    RayTracer.renderer(spheres)

if __name__ == "__main__":
    main()