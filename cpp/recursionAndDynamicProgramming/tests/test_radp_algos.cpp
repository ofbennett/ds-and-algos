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