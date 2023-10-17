from .types.objects import Vector3, RGB
from math import sqrt


class Object:
    def __init__(
        self,
        position: Vector3,
        radius: float,
        surfaceColor: RGB,
        emissionColor: RGB,
    ) -> None:
        self.position: Vector3 = position  # position of the object
        self.surfaceColor: RGB = surfaceColor  # object surface color
        self.emissionColor: RGB = emissionColor  # object surface emission (light)
        self.radius: float = radius  # Object radius
        self.squareRadius: float = radius * radius
        self.reflection: float = 0.5
        self.transparency: float = 0

    def intersect(
        self, rayOriginalDirection: Vector3, rayDirection: Vector3, t0: float, t1: float
    ) -> dict:
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
    
    def __str__(self) -> str:
        return self.__class__.__name__


class Sphere(Object):
    def __init__(
        self,
        position,
        radius,
        surfaceColor,
        emissionColor,
        width,
        height,
    ) -> None:
        super().__init__(
            position,
            radius,
            surfaceColor,
            emissionColor,
        )


class Rectangle(Object):
    def __init__(
        self,
        position: Vector3,
        radius: float,
        width: float,
        height: float,
        surfaceColor: RGB,
        emissionColor: RGB,
    ) -> None:
        super().__init__(position, radius, surfaceColor, emissionColor)
        self.width = width
        self.height = height

    def intersect(self, rayOriginalDirection, rayDirection, t0, t1):
        # Assuming the rectangle is initially in the XY plane
        normal = Vector3(0, 0, 1)

        # Calculate the D coefficient of the plane equation
        d = -normal.dot(self.position)

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
                    t0 = t - d
                    t1 = t - d
                    return {"intersects": True, "t0": t0, "t1": t1}

        # Return an empty dictionary if no intersection occurs
        return {}


class Triangle(Object):
    def __init__(
        self,
        position: Vector3,
        width: float,
        height: float,
        radius: float,
        surfaceColor: RGB,
        emissionColor: RGB,
    ) -> None:
        super().__init__(position, radius, surfaceColor, emissionColor)
        self.v0 = Vector3(0, 0, -10)
        self.v1 = Vector3(1, 0, -10)
        self.v2 = Vector3(0.5, 1, -10)

    def intersect(self, rayOriginalDirection, rayDirection, t0, t1):
        # Calculate the triangle's normal using the cross product of two edges
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        normal = edge1.cross(edge2)

        # Calculate the D coefficient of the plane equation
        d = -normal.dot(self.position)

        # Calculate the denominator of the ray-plane intersection formula
        denom = rayDirection.dot(normal)

        # Check if the ray and triangle are not parallel
        if abs(denom) > 1e-6:
            t = (self.position - rayOriginalDirection).dot(normal) / denom

            # Check if the intersection point is in front of the ray's origin
            if t > 0:
                hit_point = rayOriginalDirection + rayDirection * t

                # Calculate barycentric coordinates
                v0v1 = self.v1 - self.v0
                v0v2 = self.v2 - self.v0
                v0p = hit_point - self.v0

                dot00 = v0v1.dot(v0v1)
                dot01 = v0v1.dot(v0v2)
                dot02 = v0v1.dot(v0p)
                dot11 = v0v2.dot(v0v2)
                dot12 = v0v2.dot(v0p)

                # Calculate barycentric coordinates
                inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
                u = (dot11 * dot02 - dot01 * dot12) * inv_denom
                v = (dot00 * dot12 - dot01 * dot02) * inv_denom

                # Check if the hit point is inside the triangle
                if (u >= 0) and (v >= 0) and (u + v <= 1):
                    t0 = t - d
                    t1 = t - d
                    return {"intersects": True, "t0": t0, "t1": t1}

        # Return an empty dictionary if no intersection occurs
        return {}
