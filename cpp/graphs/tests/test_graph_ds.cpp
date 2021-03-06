#include <catch.hpp>
#include "graph_ds.h"

TEST_CASE("GraphAdjacencyList - basic test"){
    adjList adjacencyList = {{0,vecI{1,2,3}},{1,vecI{0,2}},{2,vecI{0,1}},{3,vecI{0}}};
    vecF values = {10,2,3,11};
    GraphAdjacencyList gal = GraphAdjacencyList(adjacencyList, values);
    REQUIRE(gal.values[1] == 2);
    REQUIRE(gal.adjacencyList[1][1] == 2);
    REQUIRE(gal.adjacencyList[2].size() == 2);
}

TEST_CASE("Graph - basic test"){
    adjList adjacencyList = {{0,vecI{1,2,3}},{1,vecI{0,2}},{2,vecI{0,1}},{3,vecI{0}}};
    vecF values = {10,2,3,11};
    GraphAdjacencyList gal = GraphAdjacencyList(adjacencyList, values);
    Graph graph = Graph(gal);
    REQUIRE(graph.nodePtArray[0]->value == 10);
    REQUIRE(graph.nodePtArray[0]->childrenPtArray[0] == graph.nodePtArray[1]);
    REQUIRE(graph.nodeNumber == 4);
    REQUIRE(graph.nodePtArray[1]->childNum == 2);
}