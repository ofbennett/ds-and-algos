import pytest
from random import shuffle
import random

from .. import BubbleSort

def test_basic():
    bs = BubbleSort()
    x = [2,1,3]
    y = bs.sort(x)
    assert(x == [2,1,3])
    assert(y == [1,2,3])

def test_large_list():
    N = 1000
    x = list(range(10,N))
    random.seed(12)
    shuffle(x)
    bs = BubbleSort()
    y = bs.sort(x)
    assert(y == sorted(x))

def test_edge_cases():
    bs = BubbleSort()
    x = [1]
    y = bs.sort(x)
    assert(y == [1])
    x = []
    y = bs.sort(x)
    assert(y == [])
    x = [1,1,1]
    y = bs.sort(x)
    assert(y == [1,1,1])
    x = [1,2,3]
    y = bs.sort(x)
    assert(y == [1,2,3])
