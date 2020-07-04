#include <catch.hpp>
#include "sort_algos.h"

typedef std::vector<int> vec;

TEST_CASE("Basic test"){
    vec vec1 = {3, 1, 9, 4};
    vec vec1_before = {3, 1, 9, 4};
    vec vec2 = {1, 3, 4, 9};
    BubbleSort bs = BubbleSort();
    vec vec3 = bs.sort(vec1);
    REQUIRE(vec3 == vec2);
    REQUIRE(vec1_before == vec1);
}