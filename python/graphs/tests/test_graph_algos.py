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
    adjacencyList = {0:  [1,2,3,4], 
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

@pytest.fixture
def mediumWeightedGraph():
    adjacencyList = {0:  [1,2,3], 
                     1:  [0,4], 
                     2:  [0,4,5,3], 
                     3:  [0,2,6], 
                     4:  [1,7,2], 
                     5:  [2,7,8], 
                     6:  [3,8], 
                     7:  [4,9,5], 
                     8:  [6,5,9,10], 
                     9:  [7,10,8], 
                     10: [8,9]}

    weights =       {0:  [2,1,1], 
                     1:  [2,1], 
                     2:  [1,2,3,2], 
                     3:  [1,2,4], 
                     4:  [1,4,2], 
                     5:  [3,3,2], 
                     6:  [4,2], 
                     7:  [4,1,3], 
                     8:  [2,2,5,2], 
                     9:  [1,2,5], 
                     10: [2,2]}
    gal = GraphAdjacencyList(adjacencyList, weights = weights)
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

def test_dijkstra(mediumWeightedGraph):
    gAlgo = GraphAlgos(mediumWeightedGraph)

    distance, path = gAlgo.dijkstraArray(0,5)
    assert(distance == 4)
    assert(path == [0,2,5])

    distance, path = gAlgo.dijkstraArray(0,2)
    assert(distance == 1)
    assert(path == [0,2])

    distance, path = gAlgo.dijkstraArray(4,10)
    assert(distance == 7)
    assert(path == [4,7,9,10])

    distance, path = gAlgo.dijkstraArray(0,9)
    assert(distance == 8)
    assert(path == [0,2,4,7,9])