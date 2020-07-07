#include "graph_algos.h"

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