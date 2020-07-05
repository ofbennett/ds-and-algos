import pytest
from .. import GraphAdjacencyList, Graph

@pytest.fixture
def simpleGraphAdjacencyList():
    adjacencyList = {0: [1], 1: [0,2], 2: [1]}
    values = {0: 3, 1: 5, 2: 7}
    color = {0: 'red', 1: 'blue', 2: 'green'}
    gal = GraphAdjacencyList(adjacencyList, values = values, color = color)
    return gal


def test_graphAdjacencyList(simpleGraphAdjacencyList):
    gal = simpleGraphAdjacencyList
    assert(gal.adjacencyList[2] == [1])
    assert(gal.attrDict['values'][1] == 5)
    assert(gal.attrDict['color'][1] == 'blue')

def test_graphCreation(simpleGraphAdjacencyList):
    gal = simpleGraphAdjacencyList
    graph = Graph()
    graph.buildFromAdjacencyList(gal)
    assert(len(graph.nodeArray[0].children) == 1)
    assert(graph.nodeArray[0].children[0] is graph.nodeArray[1])
    assert(graph.nodeArray[1].value == 5)
    assert(graph.nodeArray[2].attr['color'] == 'green')
    assert(len(graph.nodeArray[1].children) == 2)
    