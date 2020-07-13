#include <catch.hpp>
#include "linkedLists.h"

typedef std::vector<float> vec;

TEST_CASE("Push Pop Head test"){
    SinglyLinkedList sll = SinglyLinkedList();
    sll.pushHead(5);
    sll.pushHead(7);
    sll.pushHead(9);
    REQUIRE(sll.getHead() == 9);
    REQUIRE(sll.getTail() == 5);
    REQUIRE(sll.getLength() == 3);
    float x = sll.popHead();
    REQUIRE(x == 9);
    REQUIRE(sll.getHead() == 7);
    REQUIRE(sll.getTail() == 5);
    REQUIRE(sll.getLength() == 2);
    x = sll.popHead();
    REQUIRE(x == 7);
    REQUIRE(sll.getHead() == 5);
    REQUIRE(sll.getTail() == 5);
    REQUIRE(sll.getLength() == 1);
    x = sll.popHead();
    REQUIRE(x == 5);
    REQUIRE(sll.getLength() == 0);
}

TEST_CASE("Push Pop Tail test"){
    SinglyLinkedList sll = SinglyLinkedList();
    sll.pushTail(5);
    sll.pushTail(7);
    sll.pushTail(9);
    REQUIRE(sll.getHead() == 5);
    REQUIRE(sll.getTail() == 9);
    REQUIRE(sll.getLength() == 3);
    float x = sll.popTail();
    REQUIRE(x == 9);
    REQUIRE(sll.getHead() == 5);
    REQUIRE(sll.getTail() == 7);
    REQUIRE(sll.getLength() == 2);
    x = sll.popTail();
    REQUIRE(x == 7);
    REQUIRE(sll.getHead() == 5);
    REQUIRE(sll.getTail() == 5);
    REQUIRE(sll.getLength() == 1);
    x = sll.popTail();
    REQUIRE(x == 5);
    REQUIRE(sll.getLength() == 0);
}

TEST_CASE("Test Init with Vector"){
    vec vec1 = {1, 3, 5, 7};
    SinglyLinkedList sll1 = SinglyLinkedList(vec1);
    vec vec2 = sll1.getVector();
    REQUIRE(vec2 == vec1);

    vec vec3 = {5};
    SinglyLinkedList sll2 = SinglyLinkedList(vec3);
    vec vec4 = sll2.getVector();
    REQUIRE(vec4 == vec3);
}

TEST_CASE("Test value at method"){
    vec vec1 = {1, 3, 5, 7};
    SinglyLinkedList sll1 = SinglyLinkedList(vec1);
    REQUIRE(sll1.valueAt(0) == 1);
    REQUIRE(sll1.valueAt(1) == 3);
    REQUIRE(sll1.valueAt(2) == 5);
    REQUIRE(sll1.valueAt(3) == 7);
}

TEST_CASE("Test delete at method"){
    vec vec1 = {1, 3, 5, 7};
    vec vec2 = {1, 5, 7};
    vec vec3 = {5, 7};
    vec vec4 = {5};
    vec vec5 = {};
    SinglyLinkedList sll1 = SinglyLinkedList(vec1);
    sll1.deleteAt(1);
    REQUIRE(sll1.getVector() == vec2);
    sll1.deleteAt(0);
    REQUIRE(sll1.getVector() == vec3);
    sll1.deleteAt(1);
    REQUIRE(sll1.getVector() == vec4);
    sll1.deleteAt(0);
    REQUIRE(sll1.getVector() == vec5);

    vec vec6 = {1, 3, 5, 7};
    vec vec7 = {1, 3, 5};
    SinglyLinkedList sll2 = SinglyLinkedList(vec6);
    sll2.deleteAt(3);
    REQUIRE(sll2.getVector() == vec7);
}

TEST_CASE("Test insert at method"){
    vec vec1 = {1, 3, 5, 7};
    vec vec2 = {1, 3, 9, 5, 7};
    vec vec3 = {1, 3, 9, 5, 2, 7};
    vec vec4 = {4, 1, 3, 9, 5, 2, 7};
    SinglyLinkedList sll1 = SinglyLinkedList(vec1);
    sll1.insertAt(2,9);
    REQUIRE(sll1.getVector() == vec2);
    sll1.insertAt(4,2);
    REQUIRE(sll1.getVector() == vec3);
    sll1.insertAt(0,4);
    REQUIRE(sll1.getVector() == vec4);

    vec vec5 = {1};
    vec vec6 = {2,1};
    SinglyLinkedList sll2 = SinglyLinkedList(vec5);
    sll2.insertAt(0,2);
    REQUIRE(sll2.getVector() == vec6);
}

TEST_CASE("Test reverse in place method"){
    vec vec1 = {1, 3, 9, 5, 7};
    vec vec2 = {7, 5, 9, 3, 1};
    SinglyLinkedList sll1 = SinglyLinkedList(vec1);
    sll1.reverse();
    REQUIRE(sll1.getVector() == vec2);
    sll1.reverse();
    REQUIRE(sll1.getVector() == vec1);

    vec vec3 = {1,2};
    vec vec4 = {2,1};
    SinglyLinkedList sll2 = SinglyLinkedList(vec3);
    sll2.reverse();
    REQUIRE(sll2.getVector() == vec4);

    vec vec5 = {1};
    vec vec6 = {1};
    SinglyLinkedList sll3 = SinglyLinkedList(vec5);
    sll3.reverse();
    REQUIRE(sll3.getVector() == vec6);
}