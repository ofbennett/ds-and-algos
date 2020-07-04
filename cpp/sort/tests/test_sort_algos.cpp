#include <catch.hpp>
#include <algorithm> // std::random_shuffle
#include "sort_algos.h"

typedef std::vector<int> vec;

/////////// BubbleSort Tests ///////////

TEST_CASE("BubbleSort - Basic test"){
    vec vec1 = {3, 1, 9, 4, 2};
    vec vec1_before = {3, 1, 9, 4, 2};
    vec vec2 = {1, 2, 3, 4, 9};
    BubbleSort bs = BubbleSort();
    vec vec3 = bs.sort(vec1);
    REQUIRE(vec3 == vec2);
    REQUIRE(vec1_before == vec1);
}

TEST_CASE("BubbleSort - Edge Cases"){
    vec vec1_1 = {};
    vec vec2_1 = {};
    BubbleSort bs = BubbleSort();
    vec vec3_1 = bs.sort(vec1_1);
    REQUIRE(vec3_1 == vec2_1);

    vec vec1_2 = {1};
    vec vec2_2 = {1};
    vec vec3_2 = bs.sort(vec1_2);
    REQUIRE(vec3_2 == vec2_2);

    vec vec1_3 = {1,1,1,1,1};
    vec vec2_3 = {1,1,1,1,1};
    vec vec3_3 = bs.sort(vec1_3);
    REQUIRE(vec3_3 == vec2_3);

    vec vec1_4 = {1,2,3,4,5};
    vec vec2_4 = {1,2,3,4,5};
    vec vec3_4 = bs.sort(vec1_4);
    REQUIRE(vec3_4 == vec2_4);

    vec vec1_5 = {1,2,3,4,4,5};
    vec vec2_5 = {1,2,3,4,4,5};
    vec vec3_5 = bs.sort(vec1_5);
    REQUIRE(vec3_5 == vec2_5);
}

TEST_CASE("BubbleSort - Large List"){
    int N = 1000;
    vec vec1(N);
    std::iota(vec1.begin(), vec1.end(), 1); // Fills vec with ints in range 1 to N
    vec vec2 = vec(vec1);
    std::random_shuffle(vec1.begin(), vec1.end());

    BubbleSort bs = BubbleSort();
    vec vec3 = bs.sort(vec1);
    REQUIRE(vec3 == vec2);
}

/////////// QuickSort Tests ///////////

TEST_CASE("QuickSort - Basic test"){
    vec vec1 = {3, 1, 9, 4, 2};
    vec vec1_before = {3, 1, 9, 4, 2};
    vec vec2 = {1, 2, 3, 4, 9};
    QuickSort qs = QuickSort();
    vec vec3 = qs.sort(vec1);
    REQUIRE(vec3 == vec2);
    REQUIRE(vec1_before == vec1);
}

TEST_CASE("QuickSort - Edge Cases"){
    vec vec1_1 = {};
    vec vec2_1 = {};
    QuickSort qs = QuickSort();
    vec vec3_1 = qs.sort(vec1_1);
    REQUIRE(vec3_1 == vec2_1);

    vec vec1_2 = {1};
    vec vec2_2 = {1};
    vec vec3_2 = qs.sort(vec1_2);
    REQUIRE(vec3_2 == vec2_2);

    vec vec1_3 = {1,1,1,1,1};
    vec vec2_3 = {1,1,1,1,1};
    vec vec3_3 = qs.sort(vec1_3);
    REQUIRE(vec3_3 == vec2_3);

    vec vec1_4 = {1,2,3,4,5};
    vec vec2_4 = {1,2,3,4,5};
    vec vec3_4 = qs.sort(vec1_4);
    REQUIRE(vec3_4 == vec2_4);

    vec vec1_5 = {1,2,3,4,4,5};
    vec vec2_5 = {1,2,3,4,4,5};
    vec vec3_5 = qs.sort(vec1_5);
    REQUIRE(vec3_5 == vec2_5);
}

TEST_CASE("QuickSort - Large List"){
    int N = 1000;
    vec vec1(N);
    std::iota(vec1.begin(), vec1.end(), 1); // Fills vec with ints in range 1 to N
    vec vec2 = vec(vec1);
    std::random_shuffle(vec1.begin(), vec1.end());

    QuickSort qs = QuickSort();
    vec vec3 = qs.sort(vec1);
    REQUIRE(vec3 == vec2);
}

/////////// MergeSort Tests ///////////

TEST_CASE("MergeSort - Basic test"){
    vec vec1 = {3, 1, 9, 4, 2};
    vec vec1_before = {3, 1, 9, 4, 2};
    vec vec2 = {1, 2, 3, 4, 9};
    MergeSort ms = MergeSort();
    vec vec3 = ms.sort(vec1);
    REQUIRE(vec3 == vec2);
    REQUIRE(vec1_before == vec1);
}

TEST_CASE("MergeSort - Edge Cases"){
    vec vec1_1 = {};
    vec vec2_1 = {};
    MergeSort ms = MergeSort();
    vec vec3_1 = ms.sort(vec1_1);
    REQUIRE(vec3_1 == vec2_1);

    vec vec1_2 = {1};
    vec vec2_2 = {1};
    vec vec3_2 = ms.sort(vec1_2);
    REQUIRE(vec3_2 == vec2_2);

    vec vec1_3 = {1,1,1,1,1};
    vec vec2_3 = {1,1,1,1,1};
    vec vec3_3 = ms.sort(vec1_3);
    REQUIRE(vec3_3 == vec2_3);

    vec vec1_4 = {1,2,3,4,5};
    vec vec2_4 = {1,2,3,4,5};
    vec vec3_4 = ms.sort(vec1_4);
    REQUIRE(vec3_4 == vec2_4);

    vec vec1_5 = {1,2,3,4,4,5};
    vec vec2_5 = {1,2,3,4,4,5};
    vec vec3_5 = ms.sort(vec1_5);
    REQUIRE(vec3_5 == vec2_5);
}

TEST_CASE("MergeSort - Large List"){
    int N = 1000;
    vec vec1(N);
    std::iota(vec1.begin(), vec1.end(), 1); // Fills vec with ints in range 1 to N
    vec vec2 = vec(vec1);
    std::random_shuffle(vec1.begin(), vec1.end());

    MergeSort ms = MergeSort();
    vec vec3 = ms.sort(vec1);
    REQUIRE(vec3 == vec2);
}

    // Prints vector to cout:
    // for(int i = 0; i < vec1.size(); i++){
    //         std::cout << vec1[i] << " ";
    //     }
    // std::cout << std::endl;