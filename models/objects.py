from .types.objects import Vector3, RGB
from math import sqrt


class Object:
    def __init__(
        self,
        position: Vector3,
        radius: float,
        surfaceColor: RGB,
        emissionColor: RGB,
        transparency: float,
        reflection: float,
    ) -> None:
        self.position: Vector3 = position  # position of the object
        self.surfaceColor: RGB = surfaceColor  # object surface color
        self.emissionColor: RGB = emissionColor  # object surface emission (light)
        self.transparency: float = transparency  # object surface transparency
        self.reflection: float = reflection  # object surface reflectivity
        self.radius: float = radius  # Object radius
        self.squareRadius: float = radius * radius

    def intersect(self, rayOriginalDirection: Vector3, rayDirection: Vector3, t0: float, t1: float) -> dict:
        l: Vector3 = self.position - rayOriginalDirection
        tca: float = l.dot(rayDirection)
        if tca < 0:
            return {}
        d2: float = l.dot(l) - tca * tca
        if d2 > self.squareRadius:
            return {}
        thc: float = sqrt(self.squareRadius - d2)
        t0 = tca - thc
        t1 = tca + thc
        
        return {"intersects": True, "t0": t0, "t1": t1}

class Sphere(Object):
    def __init__(
        self,
        position,
        radius,
        surfaceColor,
        emissionColor,
        transparency,
        reflection,
    ) -> None:
        super().__init__(
            position,
            radius,
            surfaceColor,
            emissionColor,
            transparency,
            reflection,
        )


class Rectangle(Object):
    def __init__(self, position: Vector3, width: float, height: float, surfaceColor: RGB, emissionColor: RGB, transparency: float, reflection: float) -> None:
        super().__init__(position, 1, surfaceColor, emissionColor, transparency, reflection)
        self.width = width
        self.height = height

    def intersect(self, rayOriginalDirection, rayDirection, t0, t1):
        normal = Vector3(0, 0, 0)  # Assuming the rectangle is initially in the XY plane
        d = -normal.dot(self.position)  # Calculate the D coefficient of the plane equation

        # Calculate the denominator of the ray-plane intersection formula
        denom = rayDirection.dot(normal)

        # Check if the ray and plane are not parallel
        if abs(denom) > 1e-6:
            t = (-(rayOriginalDirection.dot(normal) + d)) / denom

            # Check if the intersection point is in front of the ray's origin
            if t > 0:
                hit_point = rayOriginalDirection + rayDirection * t

                # Check if the hit point is within the rectangle's bounds
                min_x = self.position.x
                max_x = self.position.x + self.width
                min_y = self.position.y
                max_y = self.position.y + self.height

                if (min_x <= hit_point.x <= max_x) and (min_y <= hit_point.y <= max_y):
                    t0 = t
                    t1 = t
                    return {"intersects": True, "t0": t0, "t1": t1}

        return {}