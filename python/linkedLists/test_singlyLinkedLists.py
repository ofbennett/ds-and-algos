import pytest
from linkedLists import SinglyLinkedList

def test_push_pop_head():
    sll = SinglyLinkedList()
    sll.push_head(5)
    sll.push_head(7)
    sll.push_head(9)
    assert(sll.get_head() == 9)
    assert(sll.get_tail() == 5)
    assert(sll.get_length() == 3)
    x = sll.pop_head()
    assert(x == 9)
    assert(sll.get_head() == 7)
    assert(sll.get_tail() == 5)
    assert(sll.get_length() == 2)
    x = sll.pop_head()
    assert(x == 7)
    assert(sll.get_head() == 5)
    assert(sll.get_tail() == 5)
    assert(sll.get_length() == 1)
    x = sll.pop_head()
    assert(x == 5)
    assert(sll.get_head() is None)
    assert(sll.get_tail() is None)
    assert(sll.get_length() == 0)
    sll.pop_head()
    assert(sll.get_head() is None)
    assert(sll.get_tail() is None)
    assert(sll.get_length() == 0)

def test_push_pop_tail():
    sll = SinglyLinkedList()
    sll.push_tail(5)
    sll.push_tail(7)
    sll.push_tail(9)
    assert(sll.get_head() == 5)
    assert(sll.get_tail() == 9)
    assert(sll.get_length() == 3)
    sll.pop_tail()
    assert(sll.get_head() == 5)
    assert(sll.get_tail() == 7)
    assert(sll.get_length() == 2)
    sll.pop_tail()
    assert(sll.get_head() == 5)
    assert(sll.get_tail() == 5)
    assert(sll.get_length() == 1)
    sll.pop_tail()
    assert(sll.get_head() is None)
    assert(sll.get_tail() is None)
    assert(sll.get_length() == 0)
    sll.pop_tail()
    assert(sll.get_head() is None)
    assert(sll.get_tail() is None)
    assert(sll.get_length() == 0)

def test_init_array():
    a = [3,5,7]
    sll = SinglyLinkedList(a)
    assert(sll.get_head() == 3)
    assert(sll.get_tail() == 7)
    assert(sll.get_length() == 3)
    assert(sll.get_list() == a)

def test_item_at():
    a = [3,5,7]
    sll = SinglyLinkedList(a)
    assert(sll.item_at(0) == 3)
    assert(sll.item_at(1) == 5)
    assert(sll.item_at(2) == 7)
    with pytest.raises(IndexError):
        sll.item_at(3)
    with pytest.raises(IndexError):
        sll.item_at(10)
    with pytest.raises(IndexError):
        sll.item_at(-1)

def test_get_list():
    a = [3,5,7]
    sll = SinglyLinkedList(a)
    b = sll.get_list()
    assert(a == b)
    c = []
    sll = SinglyLinkedList(c)
    d = sll.get_list()
    assert(c == d)

def test_delete_at():
    a = [3,5,7]
    sll = SinglyLinkedList(a)
    sll.delete_at(1)
    assert(sll.get_list() == [3,7])
    sll.delete_at(0)
    assert(sll.get_list() == [7])
    sll.delete_at(0)
    assert(sll.get_list() == [])

    a = [3,5,7,8,2,3,1]
    sll = SinglyLinkedList(a)
    sll.delete_at(3)
    assert(sll.get_list() == [3,5,7,2,3,1])
    sll.delete_at(0)
    assert(sll.get_list() == [5,7,2,3,1])
    sll.delete_at(4)
    assert(sll.get_list() == [5,7,2,3])
    with pytest.raises(IndexError):
        sll.delete_at(10)
    with pytest.raises(IndexError):
        sll.delete_at(-2)

def test_insert_at():
    a = [3,5,7,9]
    sll = SinglyLinkedList(a)
    sll.insert_at(1,2)
    assert(sll.get_list() == [3,5,1,7,9])
    sll.insert_at(8,0)
    assert(sll.get_list() == [8,3,5,1,7,9])
    sll.insert_at(2,5)
    assert(sll.get_list() == [8,3,5,1,7,2,9])

    b = [1]
    sll = SinglyLinkedList(b)
    sll.insert_at(2,0)
    assert(sll.get_list() == [2,1])
    with pytest.raises(IndexError):
        sll.insert_at(2,10)

def test_reverse():
    a = [3,5,7,9]
    sll = SinglyLinkedList(a)
    sll.reverse()
    assert(sll.get_list() == [9,7,5,3])
    sll.reverse()
    assert(sll.get_list() == a)
    b = [1,2,3,4,5,6,7,8,9]
    sll = SinglyLinkedList(b)
    sll.reverse()
    assert(sll.get_list() == [9,8,7,6,5,4,3,2,1])
    c = [1,2]
    sll = SinglyLinkedList(c)
    sll.reverse()
    assert(sll.get_list() == [2,1])
    d = [1]
    sll = SinglyLinkedList(d)
    sll.reverse()
    assert(sll.get_list() == [1])
    e = []
    sll = SinglyLinkedList(e)
    sll.reverse()
    assert(sll.get_list() == [])