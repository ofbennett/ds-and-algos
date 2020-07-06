#include <catch.hpp>
#include "graph_ds.h"

TEST_CASE("This will pass"){
    REQUIRE(1==1);
}

TEST_CASE("GraphAdjacencyList - basic test"){
    adjList adjacencyList = {{0,vecI{1,2,3}},{1,vecI{0,2}},{2,vecI{0,1}},{3,vecI{0}}};
    vecF values = {10,2,3,11};
    GraphAdjacencyList gal = GraphAdjacencyList(adjacencyList, values);
    REQUIRE(gal.values[1] == 2);
    REQUIRE(gal.adjacencyList[1][1] == 2);
    REQUIRE(gal.adjacencyList[2].size() == 2);
}