import pytest
from .. import Fibonacci, TowersOfHanoi

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

def test_towersOfHanoi():

    toh = TowersOfHanoi(1)
    toh.solve(verbose=False)
    assert(len(toh.origin) == 0)
    assert(len(toh.buffer) == 0)
    assert(list(toh.destination) == list(reversed(range(1))))

    toh = TowersOfHanoi(2)
    toh.solve(verbose=False)
    assert(len(toh.origin) == 0)
    assert(len(toh.buffer) == 0)
    assert(list(toh.destination) == list(reversed(range(2))))

    toh = TowersOfHanoi(4)
    toh.solve(verbose=False)
    assert(len(toh.origin) == 0)
    assert(len(toh.buffer) == 0)
    assert(list(toh.destination) == list(reversed(range(4))))

    toh = TowersOfHanoi(8)
    toh.solve(verbose=False)
    assert(len(toh.origin) == 0)
    assert(len(toh.buffer) == 0)
    assert(list(toh.destination) == list(reversed(range(8))))

    toh = TowersOfHanoi(16)
    toh.solve(verbose=False)
    assert(len(toh.origin) == 0)
    assert(len(toh.buffer) == 0)
    assert(list(toh.destination) == list(reversed(range(16))))