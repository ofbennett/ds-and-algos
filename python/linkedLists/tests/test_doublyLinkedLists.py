import pytest
from .. import DoublyLinkedList

def test_push_pop_head():
    dll = DoublyLinkedList()
    dll.push_head(5)
    dll.push_head(7)
    dll.push_head(9)
    dll._is_all_connected()
    assert(dll.get_head() == 9)
    assert(dll.get_tail() == 5)
    assert(dll.get_length() == 3)
    dll.pop_head()
    assert(dll.get_head() == 7)
    assert(dll.get_tail() == 5)
    assert(dll.get_length() == 2)
    dll.pop_head()
    assert(dll.get_head() == 5)
    assert(dll.get_tail() == 5)
    assert(dll.get_length() == 1)
    dll.pop_head()
    assert(dll.get_head() is None)
    assert(dll.get_tail() is None)
    assert(dll.get_length() == 0)
    dll.pop_head()
    assert(dll.get_head() is None)
    assert(dll.get_tail() is None)
    assert(dll.get_length() == 0)

def test_push_pop_tail():
    dll = DoublyLinkedList()
    dll.push_tail(5)
    dll.push_tail(7)
    dll.push_tail(9)
    dll._is_all_connected()
    assert(dll.get_head() == 5)
    assert(dll.get_tail() == 9)
    assert(dll.get_length() == 3)
    dll.pop_tail()
    assert(dll.get_head() == 5)
    assert(dll.get_tail() == 7)
    assert(dll.get_length() == 2)
    dll.pop_tail()
    assert(dll.get_head() == 5)
    assert(dll.get_tail() == 5)
    assert(dll.get_length() == 1)
    dll.pop_tail()
    assert(dll.get_head() is None)
    assert(dll.get_tail() is None)
    assert(dll.get_length() == 0)
    dll.pop_tail()
    assert(dll.get_head() is None)
    assert(dll.get_tail() is None)
    assert(dll.get_length() == 0)

def test_init_array():
    a = [3,5,7]
    dll = DoublyLinkedList(a)
    assert(dll.get_head() == 3)
    assert(dll.get_tail() == 7)
    assert(dll.get_length() == 3)
    assert(dll.get_list() == a)
    dll._is_all_connected()

def test_item_at():
    a = [3,5,7]
    dll = DoublyLinkedList(a)
    assert(dll.item_at(0) == 3)
    assert(dll.item_at(1) == 5)
    assert(dll.item_at(2) == 7)
    with pytest.raises(IndexError):
        dll.item_at(3)
    with pytest.raises(IndexError):
        dll.item_at(10)
    with pytest.raises(IndexError):
        dll.item_at(-1)

def test_get_list():
    a = [3,5,7]
    dll = DoublyLinkedList(a)
    b = dll.get_list()
    assert(a == b)
    c = []
    dll = DoublyLinkedList(c)
    d = dll.get_list()
    assert(c == d)

def test_delete_at():
    a = [3,5,7]
    dll = DoublyLinkedList(a)
    dll.delete_at(1)
    assert(dll.get_list() == [3,7])
    dll._is_all_connected()
    dll.delete_at(0)
    assert(dll.get_list() == [7])
    dll._is_all_connected()
    dll.delete_at(0)
    assert(dll.get_list() == [])
    dll._is_all_connected()

    a = [3,5,7,8,2,3,1]
    dll = DoublyLinkedList(a)
    dll.delete_at(3)
    assert(dll.get_list() == [3,5,7,2,3,1])
    dll._is_all_connected()
    dll.delete_at(0)
    assert(dll.get_list() == [5,7,2,3,1])
    dll._is_all_connected()
    with pytest.raises(IndexError):
        dll.delete_at(10)
    with pytest.raises(IndexError):
        dll.delete_at(-2)

def test_insert_at():
    a = [3,5,7,9]
    dll = DoublyLinkedList(a)
    dll.insert_at(1,2)
    assert(dll.get_list() == [3,5,1,7,9])
    dll._is_all_connected()
    dll.insert_at(8,0)
    assert(dll.get_list() == [8,3,5,1,7,9])
    dll._is_all_connected()
    dll.insert_at(2,5)
    assert(dll.get_list() == [8,3,5,1,7,2,9])
    dll._is_all_connected()

    b = [1]
    dll = DoublyLinkedList(b)
    dll.insert_at(2,0)
    assert(dll.get_list() == [2,1])
    dll._is_all_connected()
    with pytest.raises(IndexError):
        dll.insert_at(2,10)

def test_reverse():
    a = [3,5,7,9]
    dll = DoublyLinkedList(a)
    dll.reverse()
    dll._is_all_connected()
    assert(dll.get_list() == [9,7,5,3])
    dll.reverse()
    dll._is_all_connected()
    assert(dll.get_list() == a)
    b = [1,2,3,4,5,6,7,8,9]
    dll = DoublyLinkedList(b)
    dll.reverse()
    dll._is_all_connected()
    assert(dll.get_list() == [9,8,7,6,5,4,3,2,1])
    c = [1,2]
    dll = DoublyLinkedList(c)
    dll.reverse()
    dll._is_all_connected()
    assert(dll.get_list() == [2,1])
    d = [1]
    dll = DoublyLinkedList(d)
    dll.reverse()
    dll._is_all_connected()
    assert(dll.get_list() == [1])
    e = []
    dll = DoublyLinkedList(e)
    dll.reverse()
    dll._is_all_connected()
    assert(dll.get_list() == [])