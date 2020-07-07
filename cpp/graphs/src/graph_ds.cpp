#include "graph_ds.h"

GraphAdjacencyList::GraphAdjacencyList(adjList adjacencyList_init, vecF values_init){
    adjacencyList = adjacencyList_init;
    values = values_init;
}

Graph::Node::Node(int index_init, int childNum_init, float value_init = 0){
    index = index_init;
    value = value_init;
    childNum = childNum_init;
    childrenPtArray = new Node*[childNum_init];
}

Graph::Node::~Node(){
    delete childrenPtArray;
}

Graph::Graph(){
    nodeNumber = 0;
    nodePtArray = NULL;
}

Graph::Graph(GraphAdjacencyList graphAdjacencyList){
    adjList adjacencyList = graphAdjacencyList.adjacencyList;
    vecF values = graphAdjacencyList.values;
    nodeNumber = adjacencyList.size();
    // create nodes
    nodePtArray = new Node*[nodeNumber];
    for(int i = 0; i < nodeNumber; i++){
        int childNum = adjacencyList[i].size();
        nodePtArray[i] = new Node(i, childNum, values[i]);
        // give nodes their values
        nodePtArray[i]->value = values[i];
    }
    // link nodes
    for(int i = 0; i < nodeNumber; i++){
        int childNum = adjacencyList[i].size();
        Node* nodePt = nodePtArray[i];
        for(int j = 0; j < childNum; j++){
            int childIndex = adjacencyList[i][j];
            nodePt->childrenPtArray[j] = nodePtArray[childIndex];
        }
    }
}

Graph::~Graph(){
    for(int i=0; i < nodeNumber; i++){
        delete nodePtArray[i];
    }
    delete [] nodePtArray;
}