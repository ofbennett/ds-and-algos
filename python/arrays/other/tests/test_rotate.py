import pytest
from random import shuffle
import random

from .. import Rotate

def test_basic():
    rot = Rotate()

    x = [2,1,3]
    y = rot.rotate_extra_array(x,1)
    assert(x == [2,1,3])
    assert(y == [3,2,1])

    x = [1,2,3,4,5,6,7]
    y = rot.rotate_extra_array(x,3)
    assert(x == [1,2,3,4,5,6,7])
    assert(y == [5,6,7,1,2,3,4])

    x = [2,1,3]
    y = rot.rotate_cycles(x,1)
    assert(x == [2,1,3])
    assert(y == [3,2,1])

    x = [1,2,3,4,5,6,7]
    y = rot.rotate_cycles(x,3)
    assert(x == [1,2,3,4,5,6,7])
    assert(y == [5,6,7,1,2,3,4])


def test_edge_cases():
    rot = Rotate()

    x = [2,1,3]
    y = rot.rotate_extra_array(x,0)
    assert(y == [2,1,3])

    x = [2,1,3]
    y = rot.rotate_extra_array(x,3)
    assert(y == [2,1,3])

    x = [2,1,3]
    y = rot.rotate_extra_array(x,6)
    assert(y == [2,1,3])

    x = [1]
    y = rot.rotate_extra_array(x,6)
    assert(y == [1])

    x = []
    y = rot.rotate_extra_array(x,6)
    assert(y == [])

    x = [2,1,3]
    y = rot.rotate_cycles(x,0)
    assert(y == [2,1,3])

    x = [2,1,3]
    y = rot.rotate_cycles(x,3)
    assert(y == [2,1,3])

    x = [2,1,3]
    y = rot.rotate_cycles(x,6)
    assert(y == [2,1,3])

    x = [1]
    y = rot.rotate_cycles(x,6)
    assert(y == [1])

    x = []
    y = rot.rotate_cycles(x,6)
    assert(y == [])

    x = [1,2,3,4,5,6]
    y = rot.rotate_cycles(x,3)
    assert(y == [4,5,6,1,2,3])
