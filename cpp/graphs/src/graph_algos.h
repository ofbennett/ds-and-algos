#ifndef GRAPH_ALGOS_H_
#define GRAPH_ALGOS_H_

#include <vector>
#include <iostream>
#include "graph_ds.h"

class GraphAlgos{
    public:
    GraphAlgos(Graph& graph);
    Graph* graphPt;
    int countNodes();
    int countLinks();
    vecI dfsRecurse(int rootIndex);
    vecI dfsIterative(int rootIndex);
    
    private:
    void _dfsRecurse(Graph::Node* nodePt, bool* nodeIsVisited, int& nodeNumVisited, Graph::Node** visitedNodesPt);
    static bool childSort(Graph::Node* left, Graph::Node* right);
};

#endif /* GRAPH_ALGOS_H_ */