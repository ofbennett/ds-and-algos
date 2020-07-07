#ifndef GRAPH_DS_H_
#define GRAPH_DS_H_

#include <vector>
#include <map>
#include <iostream>

typedef std::vector<float> vecF;
typedef std::vector<int> vecI;
typedef std::map<int, vecI> adjList;

class GraphAdjacencyList {
    public:
    GraphAdjacencyList(adjList adjacencyList, vecF values);
    adjList adjacencyList;
    vecF values;
};

class Graph {
    class Node {
        public:
        Node(int index, int childNum, float value);
        ~Node();
        int index;
        float value;
        Node** childrenPtArray;
        int childNum;
    };

    public:
    Graph();
    Graph(GraphAdjacencyList graphAdjacencyList);
    ~Graph();
    int nodeNumber;
    Node** nodePtArray;
};

#endif /* GRAPH_DS_H_ */