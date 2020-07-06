from collections import deque

class BinaryTreeAlgos:
    def __init__(self, btree):
        self.btree = btree

    def countNodes(self):
        return len(self.btree.nodeArray)
    
    def traverse(self, order = "In-Order", method = "Recursive"):
        root = self.btree.root
        nodesVisitedList = []
        if method == "Recursive":
            self._visitNodesRecursively(root, order, nodesVisitedList)
        elif method == "Iterative":
            self._visitNodesIteratively(root, order, nodesVisitedList)
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
    
    def _visitNodesIteratively(self, root, order, nodesVisitedList):
        node = root
        nodesToBeVisited = deque()
        if order == "In-Order":
            while((node is not None) or (len(nodesToBeVisited) != 0)):
                if node is not None:
                    nodesToBeVisited.append(node)
                    node = node.left
                else:
                    node = nodesToBeVisited.pop()
                    nodesVisitedList.append(node)
                    node = node.right
        
        if order == "Pre-Order":
            while((node is not None) or (len(nodesToBeVisited) != 0)):
                if node is not None:
                    nodesVisitedList.append(node)
                    nodesToBeVisited.append(node.right)
                    node = node.left
                else:
                    node = nodesToBeVisited.pop()

        if order == "Post-Order":
            isRightChild = deque()
            while((node is not None) or (len(nodesToBeVisited) != 0)):
                if node is not None:
                    nodesToBeVisited.append(node)
                    isRightChild.append(False)
                    nodesToBeVisited.append(node.right)
                    isRightChild.append(True)
                    node = node.left
                else:
                    node = nodesToBeVisited.pop()
                    rightChild = isRightChild.pop()
                    if not rightChild:
                        nodesVisitedList.append(node)
                        node = None


