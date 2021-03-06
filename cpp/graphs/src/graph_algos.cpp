#include "graph_algos.h"
#include <list>

GraphAlgos::GraphAlgos(Graph& graph_init){
    graphPt = &graph_init;
}

int GraphAlgos::countNodes(){
    return graphPt->nodeNumber;
}

int GraphAlgos::countLinks(){
    bool** linkArray;
    int n = graphPt->nodeNumber;
    linkArray = new bool*[n];
    for(int i=0; i<n; i++){
        linkArray[i] = new bool[n];
        std::fill_n(linkArray[i], n, false);
    }

    for(int i=0; i<n; i++){
        int c = graphPt->nodePtArray[i]->childNum;
        for(int k=0; k<c; k++){
            int j = graphPt->nodePtArray[i]->childrenPtArray[k]->index;
            if(i > j){
                linkArray[i][j] = true;
            } else {
                linkArray[j][i] = true;
            }
        }
    }
    
    int sum = 0;

    for(int i = 0; i<n; i++){
        for(int j = 0; j<n; j++){
            if(linkArray[i][j]==true){
                sum++;
            }
        }
    }
    
    for(int i=0; i<n; i++){
        delete linkArray[i];
    }
    delete linkArray;

    return sum;
}

vecI GraphAlgos::dfsRecurse(int rootIndex){
    int nodeNum = this->countNodes();
    int nodeNumVisited = 0;
    bool* nodeIsVisited = new bool[nodeNum];
    std::fill_n(nodeIsVisited, nodeNum, false);
    Graph::Node** visitedNodesPt = new Graph::Node*[nodeNum];
    std::fill_n(visitedNodesPt, nodeNum, nullptr);
    Graph::Node* rootNode = graphPt->nodePtArray[rootIndex];
    this->_dfsRecurse(rootNode, nodeIsVisited, nodeNumVisited, visitedNodesPt);

    vecI visitedNodesIndices(nodeNum, -1);
    for(int i=0; i<nodeNum; i++){
        visitedNodesIndices[i] = visitedNodesPt[i]->index;
    }

    delete[] nodeIsVisited;
    delete[] visitedNodesPt;

    return visitedNodesIndices;
}

void GraphAlgos::_dfsRecurse(Graph::Node* nodePt, bool* nodeIsVisited, int& nodeNumVisited, Graph::Node** visitedNodesPt){
    if(nodeIsVisited[nodePt->index] == false){
        visitedNodesPt[nodeNumVisited] = nodePt;
        nodeIsVisited[nodePt->index] = true;
        nodeNumVisited++;
    }
    Graph::Node** childArrayCopy = new Graph::Node*[nodePt->childNum];
    for(int i = 0; i < nodePt->childNum; i++){
        childArrayCopy[i] = nodePt->childrenPtArray[i];
    }
    std::sort(childArrayCopy, childArrayCopy+(nodePt->childNum), childSort);
    for(int i = 0; i < nodePt->childNum; i++){
        if(nodeIsVisited[childArrayCopy[i]->index] == false){
            this->_dfsRecurse(childArrayCopy[i], nodeIsVisited, nodeNumVisited, visitedNodesPt);
        } 
    }
    delete[] childArrayCopy;
}

bool GraphAlgos::childSort(Graph::Node* left, Graph::Node* right){
        return left->index < right->index;
    }

vecI GraphAlgos::dfsIterative(int rootIndex){
    int nodeNum = this->countNodes();
    int nodeNumVisited = 0;
    bool* nodeIsVisited = new bool[nodeNum];
    std::fill_n(nodeIsVisited, nodeNum, false);
    Graph::Node** visitedNodesPt = new Graph::Node*[nodeNum];
    std::fill_n(visitedNodesPt, nodeNum, nullptr);
    Graph::Node* rootNode = graphPt->nodePtArray[rootIndex];
    std::list<Graph::Node*> nodeList{};
    nodeList.push_front(rootNode);
    while(!nodeList.empty()){
        Graph::Node* nodePt = nodeList.front();
        nodeList.pop_front();
        if(nodeIsVisited[nodePt->index] == false){
            visitedNodesPt[nodeNumVisited] = nodePt;
            nodeIsVisited[nodePt->index] = true;
            nodeNumVisited++;
        }
        Graph::Node** childArrayCopy = new Graph::Node*[nodePt->childNum];
        for(int i = 0; i < nodePt->childNum; i++){
            childArrayCopy[i] = nodePt->childrenPtArray[i];
        }
        std::sort(childArrayCopy, childArrayCopy+(nodePt->childNum), childSort);
        for(int i = (nodePt->childNum)-1; i >=0; i--){
            if(nodeIsVisited[childArrayCopy[i]->index] == false){
                nodeList.push_front(childArrayCopy[i]);
            } 
        }
        delete[] childArrayCopy;
    }

    vecI visitedNodesIndices(nodeNum, -1);
    for(int i=0; i<nodeNum; i++){
        visitedNodesIndices[i] = visitedNodesPt[i]->index;
    }

    delete[] nodeIsVisited;
    delete[] visitedNodesPt;

    return visitedNodesIndices;
}

vecI GraphAlgos::bfs(int rootIndex){
    int nodeNum = this->countNodes();
    int nodeNumVisited = 0;
    bool* nodeIsVisited = new bool[nodeNum];
    std::fill_n(nodeIsVisited, nodeNum, false);
    Graph::Node** visitedNodesPt = new Graph::Node*[nodeNum]; 
    std::fill_n(visitedNodesPt, nodeNum, nullptr);
    Graph::Node* rootNode = graphPt->nodePtArray[rootIndex];
    std::list<Graph::Node*> nodeList{};
    nodeList.push_front(rootNode);


    while(!nodeList.empty()){
        Graph::Node* nodePt = nodeList.front();
        nodeList.pop_front();
        if(nodeIsVisited[nodePt->index] == false){
            visitedNodesPt[nodeNumVisited] = nodePt;
            nodeIsVisited[nodePt->index] = true;
            nodeNumVisited++;
        }
        Graph::Node** childArrayCopy = new Graph::Node*[nodePt->childNum];
        for(int i = 0; i < nodePt->childNum; i++){
            childArrayCopy[i] = nodePt->childrenPtArray[i];
        }
        std::sort(childArrayCopy, childArrayCopy+(nodePt->childNum), childSort);
        for(int i = 0; i < nodePt->childNum; i++){
            if(nodeIsVisited[childArrayCopy[i]->index] == false){
                nodeList.push_back(childArrayCopy[i]);
            } 
        }
        delete[] childArrayCopy;
    }

    vecI visitedNodesIndices(nodeNum, -1);
    for(int i=0; i<nodeNum; i++){
        visitedNodesIndices[i] = visitedNodesPt[i]->index;
    }

    delete[] nodeIsVisited;
    delete[] visitedNodesPt;

    return visitedNodesIndices;
}