from collections import deque

class GraphAlgos:
    def __init__(self, graph):
        self.graph = graph

    def countNodes(self):
        return len(self.graph.nodeArray)
    
    def countLinks(self):
        s = set()
        for node in self.graph.nodeArray:
            i = node.index
            for child in node.children:
                j = child.index
                linkID = sorted([i,j])
                link = tuple(linkID)
                s.add(link)
        totalLinks = len(s)
        return totalLinks
    
    # Setting testing to True in the search functions below makes the search order unique by sorting each node's children at each stage of the search. Makes testing the functions easier. 

    def dfsRecurse(self, rootIndex, testing = False):
        for node in self.graph.nodeArray:
            node.visited = False
        visitedNodes = []
        rootNode = self.graph.nodeArray[rootIndex]
        self._dfsRecurse(rootNode, visitedNodes, testing)
        visitedIndexes = [node.index for node in visitedNodes]     
        for node in self.graph.nodeArray:
            delattr(node, 'visited')   
        return visitedIndexes
    
    def _dfsRecurse(self, node, visitedNodes, testing = False):
        if node.visited == False:
            visitedNodes.append(node)
            node.visited = True
        children = node.children
        if testing:
            children.sort(key=lambda child: child.index)
        for child in children:
            if child.visited == False:
                self._dfsRecurse(child, visitedNodes, testing)
        

    def dfsIterative(self, rootIndex, testing = False):
        for node in self.graph.nodeArray:
            node.visited = False
        rootNode = self.graph.nodeArray[rootIndex]
        visitedNodes = []
        nodeDeque = deque()
        nodeDeque.append(rootNode)
        while len(nodeDeque) != 0:
            node = nodeDeque.pop()
            if node.visited == False:
                visitedNodes.append(node)
                node.visited = True
                children = node.children
                if testing:
                    children.sort(reverse=True, key=lambda child: child.index)
                for child in children:
                    if child.visited == False:
                        nodeDeque.append(child)
        visitedIndexes = [node.index for node in visitedNodes]
        for node in self.graph.nodeArray:
            delattr(node, 'visited')
        return visitedIndexes


    def bfs(self):
        pass