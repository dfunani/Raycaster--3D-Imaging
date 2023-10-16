from app import main
from models.objects import Sphere
from models.types.objects import RGB, Vector3


def test_main():
    num: int = 5
    assert list(map(lambda x: type(x), main(num))) == [
        type(
            Sphere(
                position=Vector3(5, 5, 5),
                radius=Vector3(5, 5, 5).length(),
                squareRadius=Vector3(5, 5, 5).length(),
                surfaceColor=RGB(5, 5, 5),
                emissionColor=RGB(5, 5, 5),
                transparency=5.0,
                reflection=5.0,
            )
        )
        for i in range(num)
    ]
