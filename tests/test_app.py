from app import main
from models.objects import Sphere, Triangle
from pytest import raises

def test_app_main():
    x = 0
    y = 0
    z = -5
    radius = 1
    width = 1
    height = 1
    r = 0.8
    g = 0.1
    b = 0.1
    response = main(
        [
            ["sphere", [x, y, z, radius, width, height, r, g, b]],
            ["triangle", [x, y, z, radius, width, height, r, g, b]],
        ]
    )
    assert len(response) == 2
    assert type(response[0]) == Sphere
    assert type(response[1]) == Triangle

