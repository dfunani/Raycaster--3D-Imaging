from typing import TypedDict, Union


class Intersection(TypedDict):
    intersects: bool
    first_intersection: Union[int, float]
    second_intersection: Union[int, float]
