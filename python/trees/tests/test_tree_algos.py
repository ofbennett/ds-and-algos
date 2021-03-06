import pytest
from .. import BinaryTree, TreeAdjacencyList, BinaryTreeAlgos

@pytest.fixture
def simpleBinaryTree():
    adjacencyList = {0: [1,2], 1: [None, None], 2: [None, 3], 3: [None, None]}
    values = {0: 3, 1: 5, 2: 7, 3: 2}
    color = {0: 'red', 1: 'blue', 2: 'green', 3: 'green'}
    tal = TreeAdjacencyList(adjacencyList, values = values, color = color)
    btree = BinaryTree()
    btree.buildFromAdjacencyList(tal)
    return btree

@pytest.fixture
def mediumBinaryTree():
    adjacencyList = {0:  [1,2],
                     1:  [3, None], 
                     2:  [4, 5], 
                     3:  [6, 7],
                     4:  [None, None],
                     5:  [8, 9],
                     6:  [10, None],
                     7:  [None, None],
                     8:  [11, 12],
                     9:  [None, None],
                     10: [None, None],
                     11: [None, None],
                     12: [None, None]}
    tal = TreeAdjacencyList(adjacencyList)
    btree = BinaryTree()
    btree.buildFromAdjacencyList(tal)
    return btree

def test_simpleAlgos(simpleBinaryTree, mediumBinaryTree):
    btAlgo = BinaryTreeAlgos(simpleBinaryTree)
    assert(btAlgo.countNodes() == 4)
    assert(btAlgo.getDepth() == 3)

    btAlgo = BinaryTreeAlgos(mediumBinaryTree)
    assert(btAlgo.countNodes() == 13)
    assert(btAlgo.getDepth() == 5)

def test_binaryTreeTraversal(mediumBinaryTree):
    btAlgo = BinaryTreeAlgos(mediumBinaryTree)

    correctInOrder = [10, 6, 3, 7, 1, 0, 4, 2, 11, 8, 12, 5, 9]
    indexList = btAlgo.traverse(order = "In-Order", method = "Recursive")
    assert(indexList == correctInOrder)
    indexList = btAlgo.traverse(order = "In-Order", method = "Iterative")
    assert(indexList == correctInOrder)

    correctPreOrder = [0, 1, 3, 6, 10, 7, 2, 4, 5, 8, 11, 12, 9]
    indexList = btAlgo.traverse(order = "Pre-Order", method = "Recursive")
    assert(indexList == correctPreOrder)
    indexList = btAlgo.traverse(order = "Pre-Order", method = "Iterative")
    assert(indexList == correctPreOrder)

    correctPostOrder = [10, 6, 7, 3, 1, 4, 11, 12, 8, 9, 5, 2, 0]
    indexList = btAlgo.traverse(order = "Post-Order", method = "Recursive")
    assert(indexList == correctPostOrder)
    indexList = btAlgo.traverse(order = "Post-Order", method = "Iterative")
    assert(indexList == correctPostOrder)