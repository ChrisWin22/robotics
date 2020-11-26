import pytest
from rink import Rink


def test_is_inside():
    x=500
    y=400
    test_rink = Rink(x=x,y=y)

    assert test_rink.is_inside(x-30*test_rink.SCALAR, y-40*test_rink.SCALAR)

def test_not_is_inside():
    x=500
    y=400
    left=125
    top=125
    test_rink = Rink(x=x, y=y, left=left, top=top)
    assert not test_rink.is_inside(x*test_rink.SCALAR + left + 2, y * test_rink.SCALAR + top + 2)
    assert not test_rink.is_inside(left-2, top-2)

def test_get_scaled_x():
    x=500
    y=400
    test_rink = Rink(x=x,y=y)

    assert test_rink.get_scaled_x() == x * test_rink.SCALAR

def test_get_scaled_y():
    x=500
    y=400
    test_rink = Rink(x=x,y=y)

    assert test_rink.get_scaled_y() == y * test_rink.SCALAR