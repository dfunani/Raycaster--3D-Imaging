import os, sys
from models.objects import Rectangle, Sphere
from models.types.objects import RGB, Vector3
from simulators.raycasters import render


# // In the main function, we will create the scene which is composed of 5 spheres
# // and 1 light (which is also a sphere). Then, once the scene description is complete
# // we render that scene, by calling the render() function.
def main(numObjects: int) -> list | None:
    try:
        objects = []
        rect: Rectangle = Sphere(
            position=Vector3(-0.5, -0.5, -5),  # Position of the sphere
            radius=1,
            surfaceColor=Vector3(0.8, 0.1, 0.1),  # Green color
            reflection=0.5,
            transparency=0,
            emissionColor=Vector3(0.4, 0.8, 0.4),  # No emission
        )
        sphere: Sphere = Sphere(
            position=Vector3(0, 0.5, -5),  # Position of the sphere
            radius=1,
            surfaceColor=Vector3(0.1, 0.6, 0.1),  # Green color
            reflection=0.5,
            transparency=0,
            emissionColor=Vector3(0.1, 0.6, 0.1),  # No emission
        )
        objects.append(rect)
        objects.append(sphere)
        return objects
    except BaseException as e:
        print(e)

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("[run command] [file] [numObjects:<int>]")
        else:
            result = main(int(sys.argv[1]))
            if result:
                render(result, "test-2.ppm")
            else:
                raise BaseException("Couldn't Load Objects")
    except BaseException as e:
        print(str(e))
