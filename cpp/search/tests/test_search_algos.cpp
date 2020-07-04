#include <catch.hpp>
#include <algorithm> // std::random_shuffle
#include "search_algos.h"

typedef std::vector<int> vec;

TEST_CASE("Binary Search - basic test"){
    vec v1 = {1,2,3,4,5,6};
    BinarySearch bs = BinarySearch();
    REQUIRE(bs.recursive_search(v1,4) == true);
    REQUIRE(bs.iterative_search(v1,4) == true);
    REQUIRE(bs.recursive_search(v1,8) == false);
    REQUIRE(bs.iterative_search(v1,8) == false);
}

TEST_CASE("Binary Search - edge cases"){
    vec v1 = {4};
    BinarySearch bs = BinarySearch();
    REQUIRE(bs.recursive_search(v1,4) == true);
    REQUIRE(bs.iterative_search(v1,4) == true);
    REQUIRE(bs.recursive_search(v1,8) == false);
    REQUIRE(bs.iterative_search(v1,8) == false);

    vec v2 = {4,9,9,9,9};
    REQUIRE(bs.recursive_search(v2,4) == true);
    REQUIRE(bs.iterative_search(v2,4) == true);
    REQUIRE(bs.recursive_search(v2,8) == false);
    REQUIRE(bs.iterative_search(v2,8) == false);

    vec v3 = {};
    REQUIRE(bs.recursive_search(v3,4) == false);
    REQUIRE(bs.iterative_search(v3,4) == false);

    vec v4 = {4,4,4,4,4};
    REQUIRE(bs.recursive_search(v4,4) == true);
    REQUIRE(bs.iterative_search(v4,4) == true);
    REQUIRE(bs.recursive_search(v4,8) == false);
    REQUIRE(bs.iterative_search(v4,8) == false);
    REQUIRE(bs.recursive_search(v4,-1) == false);
    REQUIRE(bs.iterative_search(v4,-1) == false);
}

TEST_CASE("Binary Search - large list"){
    int N = 1000;
    vec v1(N);
    std::iota(v1.begin(), v1.end(), 1); // Fills vec with ints in range 1 to N
    BinarySearch bs = BinarySearch();
    REQUIRE(bs.recursive_search(v1,300) == true);
    REQUIRE(bs.iterative_search(v1,300) == true);
    REQUIRE(bs.recursive_search(v1,1) == true);
    REQUIRE(bs.iterative_search(v1,1) == true);
    REQUIRE(bs.recursive_search(v1,2000) == false);
    REQUIRE(bs.iterative_search(v1,2000) == false);
}

TEST_CASE("Sequential Search - basic test"){
    vec v1 = {1,2,3,4,5,6};
    SequentialSearch ss = SequentialSearch();
    REQUIRE(ss.search(v1,4) == true);
    REQUIRE(ss.search(v1,8) == false);
}