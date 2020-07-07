#include <catch.hpp>
#include "graph_ds.h"
#include "graph_algos.h"

class GraphFixtures{
    protected:
    Graph simpleGraph(){
        adjList adjacencyList = {{0,vecI{1,2,3}},{1,vecI{0,2}},{2,vecI{0,1}},{3,vecI{0}}};
        vecF values = {10,2,3,11};
        GraphAdjacencyList gal = GraphAdjacencyList(adjacencyList, values);
        Graph graph = Graph(gal);
        return graph;
    }

    Graph mediumGraph(){
        adjList adjacencyList = {
                                 {0,vecI{1,2,3,4}},
                                 {1,vecI{0}},
                                 {2,vecI{0}},
                                 {3,vecI{0}},
                                 {4,vecI{0,5}},
                                 {5,vecI{4,6,8,11}},
                                 {6,vecI{5,7}},
                                 {7,vecI{6}},
                                 {8,vecI{9,10,5}},
                                 {9,vecI{8}},
                                 {10,vecI{8}},
                                 {11,vecI{5}}
                                 };
        vecF values = vecF(12,0);
        GraphAdjacencyList gal = GraphAdjacencyList(adjacencyList, values);
        Graph graph = Graph(gal);
        return graph;
    }
};

TEST_CASE_METHOD(GraphFixtures,"Basic Algos tests"){
    Graph graph = simpleGraph();
    GraphAlgos gAlgo = GraphAlgos(graph);
    REQUIRE(gAlgo.countNodes()==4);
    REQUIRE(gAlgo.countLinks()==4);

    Graph graph2 = mediumGraph();
    GraphAlgos gAlgo2 = GraphAlgos(graph2);
    REQUIRE(gAlgo2.countNodes()==12);
    REQUIRE(gAlgo2.countLinks()==11);
}