import pytest
from .. import Fibonacci

def test_fibonacci():
    fb = Fibonacci()
    assert(fb.memoizationMethod(0) == 0)
    assert(fb.memoizationMethod(1) == 1)
    assert(fb.memoizationMethod(2) == 1)
    assert(fb.memoizationMethod(3) == 2)
    assert(fb.memoizationMethod(4) == 3)
    assert(fb.memoizationMethod(5) == 5)
    assert(fb.memoizationMethod(20) == 6765)
    assert(fb.memoizationMethod(100) == 354224848179261915075)
    assert(fb.memoizationMethod(200) == 280571172992510140037611932413038677189525)

    assert(fb.tabulationMethod(0) == 0)
    assert(fb.tabulationMethod(1) == 1)
    assert(fb.tabulationMethod(2) == 1)
    assert(fb.tabulationMethod(3) == 2)
    assert(fb.tabulationMethod(4) == 3)
    assert(fb.tabulationMethod(5) == 5)
    assert(fb.tabulationMethod(20) == 6765)
    assert(fb.tabulationMethod(100) == 354224848179261915075)
    assert(fb.tabulationMethod(200) == 280571172992510140037611932413038677189525)