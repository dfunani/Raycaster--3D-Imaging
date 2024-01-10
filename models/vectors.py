from math import sqrt
from typing import Union, Any
from math import sqrt
from utils.decorators import type_checker, number_greater_than_checker


class Vector3:
    @type_checker(checks=Union[int, float])
    def __init__(
        self,
        x: Union[int, float] = 0,
        y: Union[int, float] = 0,
        z: Union[int, float] = 0,
    ) -> None:
        self.x = x
        self.y = y
        self.z = z

    # Multiply
    def __mul__(self, v):
        if isinstance(v, Vector3):
            return Vector3(self.x * v.x, self.y * v.y, self.z * v.z)
        return Vector3(self.x * v, self.y * v, self.z * v)

    def __rmul__(self, v):
        return self.__mul__(v)

    # Dot Product
    def dot(self, v):
        if isinstance(v, Vector3):
            return self.x * v.x + self.y * v.y + self.z * v.z
        return self.x * v + self.y * v + self.z * v

    # Subtraction
    def __sub__(self, v):
        if isinstance(v, Vector3):
            return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)
        return Vector3(self.x - v, self.y - v, self.z - v)

    def __rsub__(self, v):
        return self.__sub__(v)

    # Comparison
    def __eq__(self, v):
        if isinstance(v, Vector3):
            return self.x == v.x and self.y == v.y and self.z == v.z
        return False

    def __ne__(self, v):
        return not self.__eq__(v)

    def __lt__(self, v):
        if isinstance(v, Vector3):
            return self.x < v.x or self.y < v.y or self.z < v.z
        return False

    def __le__(self, v):
        if isinstance(v, Vector3):
            return self.x <= v.x or self.y <= v.y or self.z <= v.z
        return False

    def __gt__(self, v):
        if isinstance(v, Vector3):
            return self.x > v.x or self.y > v.y or self.z > v.z
        return False

    def __ge__(self, v):
        if isinstance(v, Vector3):
            return self.x >= v.x or self.y >= v.y or self.z >= v.z
        return False

    # Addition
    def __add__(self, v):
        if isinstance(v, Vector3):
            return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)
        return Vector3(self.x + v, self.y + v, self.z + v)

    def __iadd__(self, v):
        if isinstance(v, Vector3):
            self.x += v.x
            self.y += v.y
            self.z += v.z
        else:
            self.x += v
            self.y += v
            self.z += v
        return self

    # Unary Negation
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    # Length Functions
    def square_length(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self):
        return sqrt(self.square_length())

    # Normalize
    def normalize(self):
        square_normal = self.square_length()
        if square_normal > 0:
            inverse_normal = 1 / sqrt(square_normal)
            self.x *= inverse_normal
            self.y *= inverse_normal
            self.z *= inverse_normal
        return self


class RGB(Vector3):
    def __init__(
        self,
        r: Union[int, float] = 0,
        g: Union[int, float] = 0,
        b: Union[int, float] = 0,
    ):
        super().__init__(x=r, y=g, z=b)
        self.r = self.x
        self.g = self.y
        self.b = self.z
