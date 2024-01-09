from typing import Union
from engines.ray_tracer import RayTracer
from models.objects import Sphere
from models.vectors import RGB, Vector3

def test_raytracer():
    raytracer = RayTracer()
    assert isinstance(raytracer.trace(Vector3(), Vector3(5,5,5), [Sphere(Vector3(), 1.00, RGB())], 1), Union[Vector3, RGB])
    