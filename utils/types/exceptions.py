from typing import TypedDict, Union

class ArgumentError(Exception):
    def __init__(self, message="Invalid argument provided"):
        self.message = message
        super().__init__(self.message)

class Intersection(TypedDict):
    intersects: bool
    first_intersection: Union[int, float]
    second_intersection: Union[int, float]
