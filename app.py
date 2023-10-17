import os, sys
from typing import Union
from models.types.objects import RGB, Vector3
from simulators.raycasters import render
from models.objects import Rectangle, Sphere, Triangle

OBJECTS = {"sphere": Sphere, "rectangle": Rectangle, "triangle": Triangle}


# // In the main function, we will create the scene which is composed of 5 spheres
# // and 1 light (which is also a sphere). Then, once the scene description is complete
# // we render that scene, by calling the render() function.
def main(objects: list) -> Union[list, None]:
    try:
        response: list = []
        for object in objects:
            try:
                obj, specs = object
                x = float(specs[0])
                y = float(specs[1])
                z = float(specs[2])
                radius = int(specs[3])
                width = int(specs[4])
                height = int(specs[5])
                r = float(specs[6])
                g = float(specs[7])
                b = float(specs[8])

                response.append(
                    OBJECTS[obj](
                        position=Vector3(x, y, z),  # Position of the sphere
                        radius=radius,
                        width=width,
                        height=height,
                        surfaceColor=Vector3(0.8, 0.1, 0.1),  # Green color
                        emissionColor=Vector3(r, g, b),  # No emission
                    )
                )
            except BaseException as ee:
                print(str(ee))
        return response
    except BaseException as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(
            "[run command] [file] filename [object]='position.x;position.y;position.z;radius;width;height;r;g;b' [objec..."
        )

    try:
        # Image export file name
        filename = sys.argv[1].replace(".", "")

        # Args deconstructed - Requested Objects and their specs
        requestedObjects: list = list(
            filter(
                lambda y: len(y) == 2 and y[0] in OBJECTS.keys(),
                list(map(lambda x: x.split("="), sys.argv)),
            )
        )

        # Desconstruct the Requested Object Specs into [position.x, position.y, position.z, radius, width, height, r, g, b, transparency, reflection]
        objects: list = list(map(lambda x: [x[0], x[1].split(";")], requestedObjects))

        image = main(objects)
        print(image)
        if image:
            render(image, filename)
        else:
            raise Exception("Couldn't Load Objects")
    except Exception as e:
        sys.exit(str(e))
