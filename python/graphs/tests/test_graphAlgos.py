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

def test_simpleAlgos(simpleGraph):
    gAlgo = GraphAlgos(simpleGraph)
    assert(gAlgo.countNodes() == 3)
    assert(gAlgo.countLinks() == 2)