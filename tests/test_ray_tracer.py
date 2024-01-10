from typing import Union
from engines.ray_tracer import RayTracer
from models.objects import Sphere
from models.vectors import RGB, Vector3
from os import listdir, remove


def test_raytracer():
    raytracer = RayTracer()
    assert isinstance(
        raytracer.trace(
            Vector3(), Vector3(5, 5, 5), [Sphere(Vector3(), 1.00, RGB())], 1
        ),
        Union[Vector3, RGB],
    )


def test_renderer():
    RayTracer.renderer(
        [Sphere(Vector3(0.0, 0, -20), 4, RGB(1.00, 0.32, 0.36), 1, 0.5)],
        "tests/output/test_renderer",
    )
    assert "test_renderer.ppm" in list(listdir("./tests/output/"))
    remove("./tests/output/test_renderer.ppm")


def test_writer():
    WIDTH = 640
    HEIGHT = 480
    image = [[[0 for _ in range(3)] for _ in range(WIDTH)] for _ in range(HEIGHT)]
    RayTracer.file_writer(image, "tests/output/test_writer")
    assert "test_writer.ppm" in list(listdir("./tests/output/"))
    remove("./tests/output/test_writer.ppm")
