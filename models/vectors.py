from typing import Union, Any
from math import sqrt
from utils.decorators import type_checker, number_greater_than_checker

class Vector3:
    @type_checker(checks=Union[int, float])
    @number_greater_than_checker()
    def __init__(
        self,
        x: Union[int, float] = 0,
        y: Union[int, float] = 0,
        z: Union[int, float] = 0,
    ) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, v: Union[int, float]) -> "Vector3":
        return Vector3(self.x * v, self.y * v, self.z * v)

    def dot(self, v: Union[int, float]) -> Union[int, float]:
        return self.x * v.x + self.y * v.y + self.z * v.z

    def __sub__(self, v: Union[int, float]) -> "Vector3":
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

    def __add__(self, v: Union[int, float]) -> "Vector3":
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    def square_length(self) -> Union[int, float]:
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self) -> Union[int, float]:
        return sqrt(self.square_length())

    def normalize(self) -> "Vector3":
        squareNormal = self.square_length()
        if squareNormal > 0:
            inverseNormal = 1 / sqrt(squareNormal)
            self.x *= inverseNormal
            self.y *= inverseNormal
            self.z *= inverseNormal
        return self


class RGB(Vector3):
    def __init__(
        self,
        r: Union[int, float] = 0,
        g: Union[int, float] = 0,
        b: Union[int, float] = 0,
    ):
        super().__init__(x=r, y=g, z=b)
