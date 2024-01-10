"""The Engine Module is responsible for
exposing render, tracing and writing
capabiltiies to the application
"""

from math import inf, pi, sqrt, tan
from typing import Union

from . import MAX_RAY_DEPTH, WIDTH, HEIGHT
from utils.helpers import blend_mix

from models.objects import Sphere
from models.vectors import RGB, Vector3
from utils.decorators import type_checker


class RayTracer:
    """Singleton class created to expose
    the the required engine components of
    the Ray Tracing Algorithm"""

    @staticmethod
    def trace(
        ray_origin: Vector3,
        ray_direction: Vector3,
        spheres: list[Sphere],
        recursion_depth: int,
    ) -> Union[Vector3, RGB]:
        """This is the main trace function. It takes a ray as argument (defined by its origin
        and direction). We test if this ray intersects any of the geometry in the scene.
        If the ray intersects an object, we compute the intersection point, the normal
        at the intersection point, and shade this point using this information.
        Shading depends on the surface property (is it transparent, reflective, diffuse).
        The function returns a color for the ray. If the ray intersects an object that
        is the color of the object at the intersection point, otherwise it returns
        the background color.
        Check if ray_direction is a unit vector (has length 1)

        Args:
            ray_origin (Vector3): Represents the source of the ray that initiates the trace.
            ray_direction (Vector3): Defines the direction in which the ray is moving.
            spheres (list[Sphere]): A list containing the
            spheres in the scene that the ray might intersect with.
            recursion_depth (int): Indicates the recursion depth, determining how many times
            the function will recursively trace secondary rays. This helps simulate effects
            like reflections or refractions.


        Returns:
            Union[Vector3, RGB]: The return value of the trace
            function represents the color observed along
            the traced ray path. It captures the resulting color or
            light information perceived after
            interacting with the scene elements, such as spheres and lighting sources.
        """

        nearest_intersection = inf
        closest_sphere: Union[None, Sphere] = None
        # find intersection of this ray with the sphere in the scene
        for sphere in spheres:
            intersects, first_intersection, second_intersection = sphere.intersect(
                ray_origin, ray_direction
            )
            if intersects:
                if first_intersection < 0:
                    first_intersection = second_intersection
                if first_intersection < nearest_intersection:
                    nearest_intersection = first_intersection
                    closest_sphere = sphere
        # if there's no intersection return black or background color
        if not closest_sphere:
            return RGB(2, 2, 2)

        # color of the ray/surfaceof the object intersected by the ray
        surfaceColor = RGB()
        # point of intersection
        intersection_hit: Vector3 = ray_origin + ray_direction * nearest_intersection
        # normal at the intersection point
        surface_normal: Vector3 = intersection_hit - closest_sphere.center
        # normalize normal direction
        surface_normal.normalize()

        # If the normal and the view direction are not opposite to each other
        # reverse the normal direction. That also means we are inside the sphere so set
        # the inside bool to true. Finally reverse the sign of IdotN which we want
        # positive.

        # add some bias to the point from which we will be tracing
        bias = 1e-4
        inside = False
        if ray_direction.dot(surface_normal) > 0:
            surface_normal = -surface_normal
            inside = True

        # Determine shading, reflections, and refractions (not fully implemented)
        if (
            closest_sphere.transparency > 0 or closest_sphere.reflection > 0
        ) and recursion_depth < MAX_RAY_DEPTH:
            # Compute shading and reflections
            facing_ratio = -ray_direction.dot(surface_normal)
            # change the mix value to tweak the effect
            fresneleffect = blend_mix(pow(1 - facing_ratio, 3), 1, 0.1)

            # compute reflection direction (not need to normalize because all vectors
            # are already normalized)
            reflection_direction: Vector3 = (
                ray_direction - surface_normal * 2 * ray_direction.dot(surface_normal)
            )
            reflection_direction.normalize()
            reflection: Vector3 = RayTracer.trace(
                intersection_hit + surface_normal * bias,
                reflection_direction,
                spheres,
                recursion_depth + 1,
            )
            refraction: Vector3 = Vector3()

            # if the sphere is also transparent compute refraction ray (transmission)
            if closest_sphere.transparency:
                refractive_index_medium = 1.1
                refractive_index_outside = (
                    refractive_index_medium if inside else 1 / refractive_index_medium
                )  # are we inside or outside the surface?
                incident_cosine = -surfaceColor.dot(ray_direction)
                k_value = 1 - refractive_index_outside * refractive_index_outside * (
                    1 - incident_cosine * incident_cosine
                )
                if k_value < 0:
                    k_value = 0
                refraction_dir: Vector3 = (
                    ray_direction * refractive_index_outside
                    + surfaceColor
                    * (refractive_index_outside * incident_cosine - sqrt(k_value))
                )
                refraction_dir.normalize()
                refraction = RayTracer.trace(
                    intersection_hit - surface_normal * bias,
                    refraction_dir,
                    spheres,
                    recursion_depth + 1,
                )

            # the result is a mix of reflection and refraction (if the sphere is transparent)
            surfaceColor = (
                reflection * fresneleffect
                + refraction * (1 - fresneleffect) * closest_sphere.transparency
            ) * closest_sphere.surfaceColor

        else:
            # it's a diffuse object, no need to raytrace any further
            for sphere in spheres:
                if sphere.emissionColor.r > 0:
                    # this is a light
                    transmission: Vector3 = Vector3(1, 1, 1)
                    lightDirection: Vector3 = sphere.center - intersection_hit
                    lightDirection.normalize()
                    for s in spheres:
                        if s != sphere:
                            (
                                intersects,
                                first_intersection,
                                second_intersection,
                            ) = s.intersect(
                                intersection_hit + surface_normal * bias,
                                lightDirection,
                            )
                            if intersects:
                                transmission = 0
                                break

                    surfaceColor += (
                        closest_sphere.surfaceColor
                        * transmission
                        * max(float(0), surface_normal.dot(lightDirection))
                        * sphere.emissionColor
                    )

        return surfaceColor + closest_sphere.emissionColor

    def renderer(spheres: list[Sphere], filename="untiled") -> None:
        """
        Renders the scene described by the spheres and saves the image to a specified filename.

        Args:
            spheres (List[Sphere]): A list of Sphere objects defining the scene.
            filename (str, optional): The name of the output file. Defaults to "untitled".
        """
        image = [[[0 for _ in range(3)] for _ in range(WIDTH)] for _ in range(HEIGHT)]
        inverseWidth = 1 / WIDTH
        inverseHeight = 1 / HEIGHT
        field_of_view = 30
        aspect_ratio = WIDTH / HEIGHT
        angle = tan(pi * 0.5 * field_of_view / 180.0)

        for y in range(HEIGHT):
            for x in range(WIDTH):
                xx = (2 * ((x + 0.5) * inverseWidth) - 1) * angle * aspect_ratio
                yy = (1 - 2 * ((y + 0.5) * inverseHeight)) * angle
                ray_direction = Vector3(xx, yy, -1)
                ray_direction.normalize()
                pixel_color = RayTracer.trace(Vector3(), ray_direction, spheres, 0)
                # Normalize color values
                r = int(min(max(0, pixel_color.x), 1) * 255)
                g = int(min(max(0, pixel_color.y), 1) * 255)
                b = int(min(max(0, pixel_color.z), 1) * 255)
                image[y][x] = [r, g, b]

        RayTracer.file_writer(image, filename)

    @staticmethod
    def file_writer(image, filename="untitled") -> None:
        """Writes the image bytes to a file.

        Args:
            image (_type_): Image Buffer to write.
            filename (str, optional): Name to be given to the exported file. Defaults to "untitled".
        """
        with open(f"./{filename}.ppm", "wb") as file:
            file.write(f"P6\n{WIDTH} {HEIGHT}\n255\n".encode())
            for row in reversed(image[::-1]):
                for pixel in row:
                    file.write(bytes(pixel))
