from typing import Union


def blend_mix(a: Union[int, float], b: Union[int, float], mix: Union[int, float]):
    return b * (mix) + a * (1 - mix)
