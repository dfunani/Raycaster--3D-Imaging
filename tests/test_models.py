from pytest import raises
from models.objects import Sphere, Triangle, Object, Rectangle
from models.types.objects import RGB, Vector3

x = 0
y = 0
z = -5
radius = 1
width = 1
height = 1
r = 0.8
g = 0.1
b = 0.1


def test_objects():
    object = Object(Vector3(x, y, z), radius, RGB(r, g, b), RGB(r, g, b))
    assert object.position.x == 0
    assert object.position.y == 0
    assert object.position.z == -5
    assert object.radius == 1
    assert object.squareRadius == 1
    assert object.emissionColor.x == 0.8
    assert object.emissionColor.y == 0.1
    assert object.emissionColor.z == 0.1

    with raises(AttributeError):
        assert object.width == 1
        assert object.height == 1


def test_spheres():
    object = Sphere(Vector3(x, y, z), radius, RGB(r, g, b), RGB(r, g, b), width, height)
    assert object.position.x == 0
    assert object.position.y == 0
    assert object.position.z == -5
    assert object.radius == 1
    assert object.emissionColor.x == 0.8
    assert object.emissionColor.y == 0.1
    assert object.emissionColor.z == 0.1

    with raises(AttributeError):
        assert object.width == 1
        assert object.height == 1


def test_rectangles():
    object = Rectangle(
        Vector3(x, y, z), radius, width, height, RGB(r, g, b), RGB(r, g, b)
    )
    assert object.position.x == 0
    assert object.position.y == 0
    assert object.position.z == -5
    assert object.radius == 1
    assert object.emissionColor.x == 0.8
    assert object.emissionColor.y == 0.1
    assert object.emissionColor.z == 0.1
    assert object.width == 1
    assert object.height == 1


def test_triangles():
    object = Triangle(
        Vector3(x, y, z), width, height, radius, RGB(r, g, b), RGB(r, g, b)
    )
    assert object.position.x == 0
    assert object.position.y == 0
    assert object.position.z == -5
    assert object.emissionColor.x == 0.8
    assert object.emissionColor.y == 0.1
    assert object.emissionColor.z == 0.1
    assert object.radius == 1

    with raises(AttributeError):
        assert object.width == 1
        assert object.height == 1

