from models.objects import Sphere
from models.vectors import Vector3, RGB
from typing import Union
from pytest import raises

from utils.types.exceptions import ArgumentError

def test_sphere():
    sphere = Sphere(Vector3(), 1.0, RGB())
    assert sphere

def test_sphere_intersection():
    sphere = Sphere(Vector3(), 1.0, RGB())
    intersect, first, second = sphere.intersect(Vector3(), Vector3())
    assert type(intersect) == bool
    assert type(first) == int or float
    assert type(second) == int or float

def test_sphere_intersection_error_args():
    with raises(ArgumentError):
        sphere = Sphere("Vector3()", 1.0, RGB())

def test_sphere_intersection_errorkwargs():
    with raises(ArgumentError):
        sphere = Sphere(Vector3(), 1.0, surfaceColor="RGB()")
        