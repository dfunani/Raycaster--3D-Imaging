from models.vectors import Vector3, RGB
from pytest import raises

from utils.types.exceptions import ArgumentError


def test_vector3():
    vector3 = Vector3()
    vector3.x == 0
    vector3.y == 0
    vector3.z == 0


def test_vector3():
    rgb = RGB(2.2, 2.2, 2.2)
    rgb.x == rgb.y == rgb.z == rgb.r == rgb.g == rgb.b == 2.2

def test_vector3_invalidarg():
    with raises(ArgumentError):
        Vector3(1, 1, "")


def test_vector3_invalidkwarg():
    with raises(ArgumentError):
        Vector3(y="")


def test_vector3_invlaidkwargarg():
    with raises(ArgumentError):
        Vector3("10", y="")

def test_vector3_invalidrgb():
    with raises(ArgumentError):
        RGB("10", b="")
