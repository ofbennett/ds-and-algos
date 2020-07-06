import pytest
from .. import Graph, GraphAdjacencyList, GraphAlgos

@pytest.fixture
def simpleGraph():
    adjacencyList = {0: [1], 1: [0,2], 2: [1]}
    values = {0: 3, 1: 5, 2: 7}
    color = {0: 'red', 1: 'blue', 2: 'green'}
    gal = GraphAdjacencyList(adjacencyList, values = values, color = color)
    graph = Graph()
    graph.buildFromAdjacencyList(gal)
    return graph

@pytest.fixture
def mediumGraph():
    adjacencyList = {0:  [1,2,3], 
                     1:  [0], 
                     2:  [0], 
                     3:  [0], 
                     4:  [0,5], 
                     5:  [4,6,8,11], 
                     6:  [5,7], 
                     7:  [6], 
                     8:  [9,10,5], 
                     9:  [8], 
                     10: [8], 
                     11: [5]}
    gal = GraphAdjacencyList(adjacencyList)
    graph = Graph()
    graph.buildFromAdjacencyList(gal)
    return graph

def test_simpleAlgos(simpleGraph, mediumGraph):
    gAlgo = GraphAlgos(simpleGraph)
    assert(gAlgo.countNodes() == 3)
    assert(gAlgo.countLinks() == 2)

    gAlgo = GraphAlgos(mediumGraph)
    assert(gAlgo.countNodes() == 12)
    assert(gAlgo.countLinks() == 11)

def test_dfs(mediumGraph):
    gAlgo = GraphAlgos(mediumGraph)
    correctOrder = [5,4,0,1,2,3,6,7,8,9,10,11]
    
    visitedIndexes = gAlgo.dfsRecurse(5, testing = True)
    assert(visitedIndexes == correctOrder)

    visitedIndexes = gAlgo.dfsIterative(5, testing = True)
    assert(visitedIndexes == correctOrder)

def test_bfs(mediumGraph):
    gAlgo = GraphAlgos(mediumGraph)
    correctOrder = [5,4,6,8,11,0,7,9,10,1,2,3]
    
    visitedIndexes = gAlgo.bfs(5, testing = True)
    assert(visitedIndexes == correctOrder)
