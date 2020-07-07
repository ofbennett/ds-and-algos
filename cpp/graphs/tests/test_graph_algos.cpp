#include <catch.hpp>
#include "graph_ds.h"
#include "graph_algos.h"

TEST_CASE("This will pass"){
    REQUIRE(1==1);
}

TEST_CASE("Basic Algos tests"){
    adjList adjacencyList = {{0,vecI{1,2,3}},{1,vecI{0,2}},{2,vecI{0,1}},{3,vecI{0}}};
    vecF values = {10,2,3,11};
    GraphAdjacencyList gal = GraphAdjacencyList(adjacencyList, values);
    Graph graph = Graph(gal);
    GraphAlgos gAlgo = GraphAlgos(graph);
    REQUIRE(gAlgo.countNodes()==4);
    REQUIRE(gAlgo.countLinks()==4);
}