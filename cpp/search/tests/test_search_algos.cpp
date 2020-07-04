#include <catch.hpp>
#include <algorithm> // std::random_shuffle
#include "search_algos.h"

typedef std::vector<int> vec;

TEST_CASE("This will pass"){
    REQUIRE(1 == 1);
}

TEST_CASE("Binary Search - basic test"){
    vec v1 = {1,2,3,4,5,6};
    BinarySearch bs = BinarySearch();
    REQUIRE(bs.recursive_search(v1,4) == true);
    REQUIRE(bs.iterative_search(v1,4) == true);
    REQUIRE(bs.recursive_search(v1,8) == false);
    REQUIRE(bs.iterative_search(v1,8) == false);
}

TEST_CASE("Sequential Search - basic test"){
    vec v1 = {1,2,3,4,5,6};
    SequentialSearch ss = SequentialSearch();
    REQUIRE(ss.search(v1,4) == true);
    REQUIRE(ss.search(v1,8) == false);
}