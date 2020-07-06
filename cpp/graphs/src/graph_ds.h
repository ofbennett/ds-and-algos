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

#endif /* GRAPH_DS_H_ */