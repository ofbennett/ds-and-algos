from collections import deque

class BinaryTreeAlgos:
    def __init__(self, btree):
        self.btree = btree

    def countNodes(self):
        return len(self.btree.nodeArray)
    
    def traverse(self, order = "In-Order"):
        root = self.btree.nodeArray[0]
        nodesVisitedList = []
        self._visitNodesRecursively(root, order, nodesVisitedList)
        nodesVisitedIndexList = [node.index for node in nodesVisitedList]
        return nodesVisitedIndexList
    
    def _visitNodesRecursively(self, node, order, nodesVisitedList):
        if order == "In-Order":
            if node.left is not None:
                self._visitNodesRecursively(node.left, order, nodesVisitedList)
            nodesVisitedList.append(node)
            if node.right is not None:
                self._visitNodesRecursively(node.right, order, nodesVisitedList)
            
        elif order == "Pre-Order":
            nodesVisitedList.append(node)
            if node.left is not None:
                self._visitNodesRecursively(node.left, order, nodesVisitedList)
            if node.right is not None:
                self._visitNodesRecursively(node.right, order, nodesVisitedList)
            
        elif order == "Post-Order":
            if node.left is not None:
                self._visitNodesRecursively(node.left, order, nodesVisitedList)
            if node.right is not None:
                self._visitNodesRecursively(node.right, order, nodesVisitedList)
            nodesVisitedList.append(node)

        else:
            raise Exception(f"Order string of {order} is invalid. Must be one of [In-Order, Pre-Order, Post-Order]")
    
    # def _visitNodesIteratively(self, node, order, nodesVisitedList):
    #     if order == "In-Order":
