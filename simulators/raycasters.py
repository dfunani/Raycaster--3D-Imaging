from math import sqrt, tan
from typing import Tuple
from models.objects import Rectangle, Sphere
from models.types.objects import RGB, Vector3
from utils import WIDTH, HEIGHT, M_PI, MAX_RAY_DEPTH
from utils.objects import mix
import pygame


def trace(rayOriginalDirection, rayDirection, objects, depth) -> Vector3:
    tnear = float("inf")
    intersected_object = None

    for obj in objects:
        t0 = float("inf")
        t1 = float("inf")
        intersects = obj.intersect(rayOriginalDirection, rayDirection, t0, t1)

        if intersects.get("intersects"):
            if intersects.get("t0") < 0:
                intersects["t0"] = intersects.get("t1")

            if intersects.get("t0") < tnear:
                tnear = intersects.get("t0")
                intersected_object = obj

    if not intersected_object:
        return Vector3(0, 0, 0)

    # color of the ray/surfaceof the object intersected by the ray
    # surfaceColor: Vector3 = RGB(0, 0, 0)
    # point of intersection
    phit: Vector3 = rayOriginalDirection + rayDirection * tnear
    # normal at the intersection point
    nhit: Vector3 = phit - intersected_object.position
    # normalize normal direction
    nhit.normalize()

    # If the normal and the view direction are not opposite to each other
    # reverse the normal direction. That also means we are inside the sphere so set
    # the inside bool to true. Finally reverse the sign of IdotN which we want
    # positive.

    # add some bias to the point from which we will be tracing
    bias: float = 1e-4
    inside: bool = False

    if rayDirection.dot(nhit) > 0:
        nhit = -nhit
        inside = True

    if (
        intersected_object.transparency > 0 or intersected_object.reflection > 0
    ) and depth < MAX_RAY_DEPTH:
        facingratio: float = -rayDirection.dot(nhit)
        # change the mix value to tweak the effect
        fresneleffect: float = mix(pow(1 - facingratio, 3), 1, 0.1)
        # compute reflection direction (not need to normalize because all vectors
        # are already normalized)
        refldir: Vector3 = rayDirection - nhit * 2 * rayDirection.dot(nhit)
        refldir.normalize()
        reflection: Vector3 = trace(phit + nhit * bias, refldir, objects, depth + 1)
        refraction: Vector3 = Vector3(0, 0, 0)
        # if the sphere is also transparent compute refraction ray (transmission)
        if intersected_object.transparency:
            ior: float = 1.1
            eta = ior if (inside) else 1 / ior  # are we inside or outside the surface?
            cosi: float = -nhit.dot(rayDirection)
            k: float = 1 - eta * eta * (1 - cosi * cosi)
            refrdir: Vector3 = rayDirection * eta + nhit * (eta * cosi - sqrt(k))
            refrdir.normalize()
            refraction = trace(phit - nhit * bias, refrdir, objects, depth + 1)

        # the result is a mix of reflection and refraction (if the sphere is transparent)
        surfaceColor = (
            reflection * fresneleffect
            + refraction * (1 - fresneleffect) * intersected_object.transparency
        ) * intersected_object.surfaceColor

    else:
        # it's a diffuse object, no need to raytrace any further
        for s in objects:
            if s.emissionColor.x > 0:
                # this is a light
                transmission: RGB = RGB(1, 1, 1)
                lightDirection: Vector3 = s.position - phit
                lightDirection.normalize()
                for j in objects:
                    if s != j:
                        t0: float = float("inf")
                        t1: float = float("inf")
                        if j.intersect(phit + nhit * bias, lightDirection, t0, t1):
                            transmission = RGB(0, 0, 0)
                            break
                surfaceColor += (
                    intersected_object.surfaceColor
                    * transmission
                    * max((0), nhit.dot(lightDirection))
                    * s.emissionColor
                )

    return surfaceColor + intersected_object.emissionColor


# Main rendering function. We compute a camera ray for each pixel of the image
# trace it and return a color. If the ray hits a sphere, we return the color of the
# sphere at the intersection point, else we return the background color.
def render(spheres: list, filename: str, fov: float = 30) -> None:
    image: Tuple[int, int] = pygame.Surface((WIDTH, HEIGHT))
    invWidth: float = 1 / float(WIDTH)
    invHeight: float = 1 / float(HEIGHT)
    aspectratio: float = WIDTH / float(HEIGHT)
    angle: float = tan(M_PI * 0.5 * fov / 180.0)
    # Trace rays
    for y in range(HEIGHT):
        for x in range(WIDTH):
            xx: float = (2 * ((x + 0.5) * invWidth) - 1) * angle * aspectratio
            yy: float = (1 - 2 * ((y + 0.5) * invHeight)) * angle
            rayDirection = Vector3(xx, yy, -1)
            rayDirection.normalize()
            pixel = trace(Vector3(0, 0, 0), rayDirection, spheres, 0)
            image.set_at(
                (x, y),
                (
                    int(min(1, pixel.x) * 255),
                    int(min(1, pixel.y) * 255),
                    int(min(1, pixel.z) * 255),
                ),
            )

    # Save result to a PPM image (keep these flags if you compile under Windows)
    with open(filename, "wb") as ppm_file:
        ppm_file.write(bytearray("P6\n", "utf-8"))
        ppm_file.write(bytearray(f"{WIDTH} {HEIGHT}\n255\n", "utf-8"))
        for y in range(HEIGHT):
            for x in range(WIDTH):
                color = image.get_at((x, y))
                ppm_file.write(bytearray([color.r, color.g, color.b]))
