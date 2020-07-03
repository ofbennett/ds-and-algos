import pytest
from random import shuffle
import random

from .. import QuickSort

def test_basic():
    qs = QuickSort()
    x = [2,1,3]
    y = qs.sort(x)
    assert(x == [2,1,3])
    assert(y == [1,2,3])

def test_large_list():
    N = 1000
    x = list(range(10,N))
    random.seed(12)
    shuffle(x)
    qs = QuickSort()
    y = qs.sort(x)
    assert(y == sorted(x))

def test_edge_cases():
    qs = QuickSort()
    x = [1]
    y = qs.sort(x)
    assert(y == [1])
    x = []
    y = qs.sort(x)
    assert(y == [])
    x = [1,1,1,1,1]
    y = qs.sort(x)
    assert(y == [1,1,1,1,1])
    x = [1,2,3,4]
    y = qs.sort(x)
    assert(y == [1,2,3,4])
    x = [1,2,3,3,4]
    y = qs.sort(x)
    assert(y == [1,2,3,3,4])
