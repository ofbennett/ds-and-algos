from collections import deque

class BinaryTreeAlgos:
    def __init__(self, btree):
        self.btree = btree

    def countNodes(self):
        return len(self.btree.nodeArray)
    