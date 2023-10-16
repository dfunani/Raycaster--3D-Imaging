from typing import Self, Union
from math import sqrt


class Vector3:
    def __init__(
        self, x: Union[int, float], y: Union[int, float], z: Union[int, float]
    ) -> None:
        self.x, self.y, self.z = x, y, z

    def length(self):
        return sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def normalize(self):
        length = self.length()
        if length > 0:
            inv_length = 1 / length
            self.x *= inv_length
            self.y *= inv_length
            self.z *= inv_length

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __add__(self, other: Self) -> Self:
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Self) -> Self:
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, value: Union[int, float, Self]) -> Self:
        if type(value) == RGB or type(value) == Vector3:
            return Vector3(self.x * value.x, self.y * value.y, self.z * value.z)
        return Vector3(self.x * value, self.y * value, self.z * value)

    def __eq__(self, value: Self) -> bool:
        if type(value) == Vector3:
            return self.x == value.x and self.y == value.y and self.z == value.z

    def __ne__(self, value: Self) -> bool:
        if type(value) == Vector3:
            return self.x != value.x or self.y != value.y or self.z != value.z


class RGB(Vector3):
    def __init__(
        self, x: Union[int, float], y: Union[int, float], z: Union[int, float]
    ) -> None:
        super().__init__(x, y, z)
