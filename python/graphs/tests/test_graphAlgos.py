import pytest
from .. import Graph, GraphAdjacencyList, GraphAlgos

@pytest.fixture
def simpleGraphAdjacencyList():
    adjacencyList = {0: [1], 1: [0,2], 2: [1]}
    values = {0: 3, 1: 5, 2: 7}
    color = {0: 'red', 1: 'blue', 2: 'green'}
    gal = GraphAdjacencyList(adjacencyList, values = values, color = color)
    return gal

def test_simpleAlgos(simpleGraphAdjacencyList):
    gal = simpleGraphAdjacencyList
    graph = Graph()
    graph.buildFromAdjacencyList(gal)
    gAlgo = GraphAlgos(graph)
    assert(gAlgo.countNodes() == 3)