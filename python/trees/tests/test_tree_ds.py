import pytest
from .. import BinaryTree, TreeAdjacencyList

@pytest.fixture
def simpleBinaryTreeAdjacencyList():
    adjacencyList = {0: [1,2], 1: [None, None], 2: [None, 3], 3: [None, None]}
    values = {0: 3, 1: 5, 2: 7, 3: 2}
    color = {0: 'red', 1: 'blue', 2: 'green', 3: 'green'}
    tal = TreeAdjacencyList(adjacencyList, values = values, color = color)
    return tal

def test_treeAdjacencyList(simpleBinaryTreeAdjacencyList):
    tal = simpleBinaryTreeAdjacencyList
    assert(tal.adjacencyList[2] == [None, 3])
    assert(tal.attrDict['values'][1] == 5)
    assert(tal.attrDict['color'][1] == 'blue')

def test_binaryTreeCreation(simpleBinaryTreeAdjacencyList):
    tal = simpleBinaryTreeAdjacencyList
    btree = BinaryTree()
    btree.buildFromAdjacencyList(tal)
    assert(btree.root is btree.nodeArray[0])
    assert(btree.nodeArray[2].right is btree.nodeArray[3])
    assert(btree.nodeArray[0].value == 3)
    assert(btree.nodeArray[1].attr["color"] == 'blue')
    assert(btree.nodeArray[1].right is None)