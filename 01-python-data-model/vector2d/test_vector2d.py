import pytest
from vector2d import Vector

def test_vector_initialization():
    v1 = Vector()
    assert v1.x == 0 and v1.y == 0

    v2 = Vector(3,4)

    assert v2.x == 3 and v2.y ==4

def test_vector_representation():
    v = Vector(1,2)
    assert repr(v) == 'Vector(1,2)'

def test_vector_magnitude():
    v = Vector(3,4)
    assert abs(v) == 5

def test_vector_boolean():
    v1 = Vector(0,0)
    assert bool(v1) is False

    v2 = Vector(1,0)
    assert bool(v2) is True

def test_vector_addition():
    v1 = Vector(2,3)
    v2 = Vector(-1,2)
    result = v1 + v2
    assert result.x ==1
    assert result.y == 5

def test_vector_multiplication():
    v= Vector(3,4)
    result = v * 2
    assert result.x == 6
    assert result.y == 8
