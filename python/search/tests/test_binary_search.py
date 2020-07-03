import pytest

from .. import BinarySearch, SequentialSearch

def test_basic():
    x = [2,3,5,6,7,9,11,14]
    bs = BinarySearch()
    answer = bs.recursive_search(x,11)
    assert(answer == True)
    answer = bs.recursive_search(x,8)
    assert(answer == False)

    answer = bs.iterative_search(x,11)
    assert(answer == True)
    answer = bs.iterative_search(x,8)
    assert(answer == False)

def test_edge_case():
    x = [2,3,5,6,7,9,11,14]
    bs = BinarySearch()
    answer = bs.recursive_search(x,14)
    assert(answer == True)
    answer = bs.recursive_search(x,0)
    assert(answer == False)
    answer = bs.recursive_search(x,2)
    assert(answer == True)
    answer = bs.recursive_search(x,-1)
    assert(answer == False)

    answer = bs.iterative_search(x,14)
    assert(answer == True)
    answer = bs.iterative_search(x,0)
    assert(answer == False)
    answer = bs.iterative_search(x,2)
    assert(answer == True)
    answer = bs.iterative_search(x,-1)
    assert(answer == False)

def test_large_array():
    x = list(range(1,1000))
    bs = BinarySearch()
    answer = bs.recursive_search(x,300)
    assert(answer == True)
    answer = bs.recursive_search(x,2000)
    assert(answer == False)

    answer = bs.iterative_search(x,300)
    assert(answer == True)
    answer = bs.iterative_search(x,2000)
    assert(answer == False)

def test_sequential_search():
    x = [2,3,5,6,7,9,11,14]
    ss = SequentialSearch()
    answer = ss.search(x,11)
    assert(answer == True)
    answer = ss.search(x,8)
    assert(answer == False)
    answer = ss.search(x,14)
    assert(answer == True)
    answer = ss.search(x,0)
    assert(answer == False)