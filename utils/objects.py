def mix(a: float, b: float, mix: callable) -> float:
    return b * mix + a * (1 - mix)