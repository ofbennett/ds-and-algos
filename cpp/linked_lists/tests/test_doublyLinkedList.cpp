#include <catch.hpp>
#include "linkedLists.h"

typedef std::vector<float> vec;

TEST_CASE("Push Pop Head test"){
    DoublyLinkedList dll = DoublyLinkedList();
    dll.pushHead(5);
    dll.pushHead(7);
    dll.pushHead(9);
    REQUIRE(dll.is_connected() == true);
    REQUIRE(dll.getHead() == 9);
    REQUIRE(dll.getTail() == 5);
    REQUIRE(dll.getLength() == 3);
    float x = dll.popHead();
    REQUIRE(x == 9);
    REQUIRE(dll.is_connected() == true);
    REQUIRE(dll.getHead() == 7);
    REQUIRE(dll.getTail() == 5);
    REQUIRE(dll.getLength() == 2);
    x = dll.popHead();
    REQUIRE(x == 7);
    REQUIRE(dll.is_connected() == true);
    REQUIRE(dll.getHead() == 5);
    REQUIRE(dll.getTail() == 5);
    REQUIRE(dll.getLength() == 1);
    x = dll.popHead();
    REQUIRE(x == 5);
    REQUIRE(dll.is_connected() == true);
    REQUIRE(dll.getLength() == 0);
}

TEST_CASE("Push Pop Tail test"){
    DoublyLinkedList dll = DoublyLinkedList();
    dll.pushTail(5);
    dll.pushTail(7);
    dll.pushTail(9);
    REQUIRE(dll.is_connected() == true);
    REQUIRE(dll.getHead() == 5);
    REQUIRE(dll.getTail() == 9);
    REQUIRE(dll.getLength() == 3);
    float x = dll.popTail();
    REQUIRE(x == 9);
    REQUIRE(dll.is_connected() == true);
    REQUIRE(dll.getHead() == 5);
    REQUIRE(dll.getTail() == 7);
    REQUIRE(dll.getLength() == 2);
    x = dll.popTail();
    REQUIRE(x == 7);
    REQUIRE(dll.is_connected() == true);
    REQUIRE(dll.getHead() == 5);
    REQUIRE(dll.getTail() == 5);
    REQUIRE(dll.getLength() == 1);
    x = dll.popTail();
    REQUIRE(x == 5);
    REQUIRE(dll.is_connected() == true);
    REQUIRE(dll.getLength() == 0);
}

TEST_CASE("Test Init with Vector"){
    vec vec1 = {1, 3, 5, 7};
    DoublyLinkedList dll1 = DoublyLinkedList(vec1);
    REQUIRE(dll1.is_connected() == true);
    vec vec2 = dll1.getVector();
    REQUIRE(vec2 == vec1);

    vec vec3 = {5};
    DoublyLinkedList dll2 = DoublyLinkedList(vec3);
    REQUIRE(dll2.is_connected() == true);
    vec vec4 = dll2.getVector();
    REQUIRE(vec4 == vec3);
}

TEST_CASE("Test value at method"){
    vec vec1 = {1, 3, 5, 7};
    DoublyLinkedList dll1 = DoublyLinkedList(vec1);
    REQUIRE(dll1.valueAt(0) == 1);
    REQUIRE(dll1.valueAt(1) == 3);
    REQUIRE(dll1.valueAt(2) == 5);
    REQUIRE(dll1.valueAt(3) == 7);
}

TEST_CASE("Test delete at method"){
    vec vec1 = {1, 3, 5, 7};
    vec vec2 = {1, 5, 7};
    vec vec3 = {5, 7};
    vec vec4 = {5};
    vec vec5 = {};
    DoublyLinkedList dll1 = DoublyLinkedList(vec1);
    dll1.deleteAt(1);
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec2);
    dll1.deleteAt(0);
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec3);
    dll1.deleteAt(1);
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec4);
    dll1.deleteAt(0);
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec5);

    vec vec6 = {1, 3, 5, 7};
    vec vec7 = {1, 3, 5};
    DoublyLinkedList dll2 = DoublyLinkedList(vec6);
    dll2.deleteAt(3);
    REQUIRE(dll2.is_connected() == true);
    REQUIRE(dll2.getVector() == vec7);
}

TEST_CASE("Test insert at method"){
    vec vec1 = {1, 3, 5, 7};
    vec vec2 = {1, 3, 9, 5, 7};
    vec vec3 = {1, 3, 9, 5, 2, 7};
    vec vec4 = {4, 1, 3, 9, 5, 2, 7};
    DoublyLinkedList dll1 = DoublyLinkedList(vec1);
    dll1.insertAt(2,9);
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec2);
    dll1.insertAt(4,2);
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec3);
    dll1.insertAt(0,4);
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec4);

    vec vec5 = {1};
    vec vec6 = {2,1};
    DoublyLinkedList dll2 = DoublyLinkedList(vec5);
    dll2.insertAt(0,2);
    REQUIRE(dll2.is_connected() == true);
    REQUIRE(dll2.getVector() == vec6);
}

TEST_CASE("Test reverse in place method"){
    vec vec1 = {1, 3, 9, 5, 7};
    vec vec2 = {7, 5, 9, 3, 1};
    DoublyLinkedList dll1 = DoublyLinkedList(vec1);
    dll1.reverse();
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec2);
    dll1.reverse();
    REQUIRE(dll1.is_connected() == true);
    REQUIRE(dll1.getVector() == vec1);

    vec vec3 = {1,2};
    vec vec4 = {2,1};
    DoublyLinkedList dll2 = DoublyLinkedList(vec3);
    dll2.reverse();
    REQUIRE(dll2.is_connected() == true);
    REQUIRE(dll2.getVector() == vec4);

    vec vec5 = {1};
    vec vec6 = {1};
    DoublyLinkedList dll3 = DoublyLinkedList(vec5);
    dll3.reverse();
    REQUIRE(dll3.is_connected() == true);
    REQUIRE(dll3.getVector() == vec6);
}
