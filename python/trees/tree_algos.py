from collections import deque

class BinaryTreeAlgos:
    def __init__(self, btree):
        self.btree = btree

    def countNodes(self):
        return len(self.btree.nodeArray)
    
    def traverse(self, order = "In-Order"):
        root = self.btree.nodeArray[0]
        nodeVisitedList = []
        self._visitNodesRecursively(root, order, nodeVisitedList)
        nodeVisitedIndexList = [node.index for node in nodeVisitedList]
        return nodeVisitedIndexList
    
    def _visitNodesRecursively(self, node, order, nodeVisitedList):
        if order == "In-Order":
            if node.left is not None:
                self._visitNodesRecursively(node.left, order, nodeVisitedList)
            nodeVisitedList.append(node)
            if node.right is not None:
                self._visitNodesRecursively(node.right, order, nodeVisitedList)
            
        elif order == "Pre-Order":
            nodeVisitedList.append(node)
            if node.left is not None:
                self._visitNodesRecursively(node.left, order, nodeVisitedList)
            if node.right is not None:
                self._visitNodesRecursively(node.right, order, nodeVisitedList)
            
        elif order == "Post-Order":
            if node.left is not None:
                self._visitNodesRecursively(node.left, order, nodeVisitedList)
            if node.right is not None:
                self._visitNodesRecursively(node.right, order, nodeVisitedList)
            nodeVisitedList.append(node)
            
        else:
            raise Exception(f"Order string of {order} is invalid. Must be one of [In-Order, Pre-Order, Post-Order]")