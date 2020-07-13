#include <catch.hpp>
#include "radp_algos.h"

TEST_CASE("Test Fibonacci algorithms"){
    Fibonacci fib = Fibonacci();
    REQUIRE(fib.tabulationMethod(0) == 0);
    REQUIRE(fib.tabulationMethod(1) == 1);
    REQUIRE(fib.tabulationMethod(2) == 1);
    REQUIRE(fib.tabulationMethod(3) == 2);
    REQUIRE(fib.tabulationMethod(4) == 3);
    REQUIRE(fib.tabulationMethod(5) == 5);
    REQUIRE(fib.tabulationMethod(20) == 6765);
    REQUIRE(fib.tabulationMethod(30) == 832040);

    REQUIRE(fib.memoizationMethod(0) == 0);
    REQUIRE(fib.memoizationMethod(1) == 1);
    REQUIRE(fib.memoizationMethod(2) == 1);
    REQUIRE(fib.memoizationMethod(3) == 2);
    REQUIRE(fib.memoizationMethod(4) == 3);
    REQUIRE(fib.memoizationMethod(5) == 5);
    REQUIRE(fib.memoizationMethod(20) == 6765);
    REQUIRE(fib.memoizationMethod (30) == 832040);
}

TEST_CASE("Test Towers Of Hanoi algorithm"){
    TowersOfHanoi toh = TowersOfHanoi(1);
    toh.solve();
    std::list<int> correctFinalTower = {0};
    REQUIRE(toh.destination == correctFinalTower);
    REQUIRE(toh.origin.size() == 0);
    REQUIRE(toh.buffer.size() == 0);

    TowersOfHanoi toh2 = TowersOfHanoi(2);
    toh2.solve();
    std::list<int> correctFinalTower2 = {1, 0};
    REQUIRE(toh2.destination == correctFinalTower2);
    REQUIRE(toh2.origin.size() == 0);
    REQUIRE(toh2.buffer.size() == 0);

    TowersOfHanoi toh3 = TowersOfHanoi(3);
    toh3.solve();
    std::list<int> correctFinalTower3 = {2, 1, 0};
    REQUIRE(toh3.destination == correctFinalTower3);
    REQUIRE(toh3.origin.size() == 0);
    REQUIRE(toh3.buffer.size() == 0);

    TowersOfHanoi toh4 = TowersOfHanoi(4);
    toh4.solve();
    std::list<int> correctFinalTower4 = {3, 2, 1, 0};
    REQUIRE(toh4.destination == correctFinalTower4);
    REQUIRE(toh4.origin.size() == 0);
    REQUIRE(toh4.buffer.size() == 0);

    TowersOfHanoi toh6 = TowersOfHanoi(6);
    toh6.solve();
    std::list<int> correctFinalTower6 = {5, 4, 3, 2, 1, 0};
    REQUIRE(toh6.destination == correctFinalTower6);
    REQUIRE(toh6.origin.size() == 0);
    REQUIRE(toh6.buffer.size() == 0);

    TowersOfHanoi toh10 = TowersOfHanoi(10);
    toh10.solve();
    std::list<int> correctFinalTower10 = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    REQUIRE(toh10.destination == correctFinalTower10);
    REQUIRE(toh10.origin.size() == 0);
    REQUIRE(toh10.buffer.size() == 0);
}