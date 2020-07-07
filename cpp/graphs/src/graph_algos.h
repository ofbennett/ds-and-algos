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
};

#endif /* GRAPH_ALGOS_H_ */