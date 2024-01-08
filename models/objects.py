from typing import Union, TypedDict
from models.vectors import Vector3, RGB
from math import sqrt
from utils.decorators import type_checker, number_greater_than_checker
from utils.types.exceptions import Intersection


class Sphere:
    @type_checker(
        checks={
            "center": Vector3,
            "radius": Union[int, float],
            "surfaceColor": RGB,
            "reflection": Union[int, float],
            "transparency": Union[int, float],
            "emissionColor": Vector3(),
        }
    )
    @number_greater_than_checker()
    def __init__(
        self,
        center: Vector3,
        radius: Union[int, float],
        surfaceColor: RGB,
        reflection: Union[int, float] = 0,
        transparency: Union[int, float] = 0,
        emissionColor: Vector3 = Vector3(),
    ) -> None:
        self.center = center
        self.radius = radius
        self.squareRadius = radius * radius
        self.surfaceColor = surfaceColor
        self.emissionColor = emissionColor
        self.transparency = transparency
        self.reflection = reflection

    @type_checker(checks=Vector3)
    def intersect(self, ray_origin: Vector3, ray_direction: Vector3) -> Intersection:
        ray_to_sphere_center = self.center - ray_origin
        projection = ray_to_sphere_center.dot(ray_direction)

        if projection < 0:
            return {
                "intersects": False,
                "first_intersection": 0,
                "second_intersection": 0,
            }

        distance_squared = (
            ray_to_sphere_center.dot(ray_to_sphere_center) - projection * projection
        )

        if distance_squared > self.squareRadius:
            return {
                "intersects": False,
                "first_intersection": 0,
                "second_intersection": 0,
            }

        distance_to_surface = sqrt(self.squareRadius - distance_squared)
        first_intersection = projection - distance_to_surface
        second_intersection = projection + distance_to_surface

        return {
            "intersects": True,
            "first_intersection": first_intersection,
            "second_intersection": second_intersection,
        }
