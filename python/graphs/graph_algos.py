from collections import deque
import heapq

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
    
    # Setting testing to True in the search functions below makes the search order unique 
    # by sorting each node's children at each stage of the search. Makes testing the functions easier. 

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


    def bfs(self, rootIndex, testing = False):
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
                    children.sort(key=lambda child: child.index)
                for child in children:
                    if child.visited == False:
                        nodeDeque.appendleft(child)
        visitedIndexes = [node.index for node in visitedNodes]
        for node in self.graph.nodeArray:
            delattr(node, 'visited')
        return visitedIndexes
    
    def dijkstraArray(self, sourceIndex, targetIndex):
        def getWeight(currentNodeIndex, childIndex):
            currentNode = self.graph.nodeArray[currentNodeIndex]
            childrenOfCurrent = currentNode.children
            childrenIndices = [child.index for child in childrenOfCurrent]
            weight = currentNode.attr['weights'][childrenIndices.index(childIndex)]
            return weight
        
        def currentMinDistance(nodeIndexSet, nodeDist):
            currentMinValue = float('inf')
            currentMinIndex = None
            for nodeIndex in nodeIndexSet:
                if nodeDist[nodeIndex] < currentMinValue:
                    currentMinValue = nodeDist[nodeIndex]
                    currentMinIndex = nodeIndex
            return currentMinIndex

        nodeIndexSet = set(range(len(self.graph.nodeArray)))
        nodeDist = [float('inf')]*len(self.graph.nodeArray)
        nodePrev = [None]*len(self.graph.nodeArray)
        nodeDist[sourceIndex] = 0
        while len(nodeIndexSet) != 0:
            currentNodeIndex = currentMinDistance(nodeIndexSet, nodeDist)
            nodeIndexSet.remove(currentNodeIndex)
            for child in self.graph.nodeArray[currentNodeIndex].children:
                childIndex = child.index
                if childIndex in nodeIndexSet:
                    currentDistance = nodeDist[currentNodeIndex] + getWeight(currentNodeIndex, childIndex)
                    if currentDistance < nodeDist[childIndex]:
                        nodeDist[childIndex] = currentDistance
                        nodePrev[childIndex] = currentNodeIndex
        
        shortestDistance = nodeDist[targetIndex]
        shortestPath = []
        current = targetIndex
        while current != sourceIndex:
            shortestPath = [current] + shortestPath
            current = nodePrev[current]
        shortestPath = [current] + shortestPath  
        return shortestDistance, shortestPath
    
    def dijkstraPriorityQueue(self, sourceIndex, targetIndex):
        def getWeight(currentNodeIndex, childIndex):
            currentNode = self.graph.nodeArray[currentNodeIndex]
            childrenOfCurrent = currentNode.children
            childrenIndices = [child.index for child in childrenOfCurrent]
            weight = currentNode.attr['weights'][childrenIndices.index(childIndex)]
            return weight

        nodeIndexSet = set(range(len(self.graph.nodeArray)))
        nodePriorityQueue = zip([float('inf')]*len(self.graph.nodeArray), range(len(self.graph.nodeArray)))
        nodePriorityQueue = list(nodePriorityQueue)
        invalidTuples = set()
        nodeDist = [float('inf')]*len(self.graph.nodeArray)
        nodePrev = [None]*len(self.graph.nodeArray)
        nodePriorityQueue[sourceIndex] = (0,sourceIndex)
        nodeDist[sourceIndex] = 0
        heapq.heapify(nodePriorityQueue)
        while len(nodePriorityQueue) != 0:
            tup = heapq.heappop(nodePriorityQueue)
            while tup in invalidTuples:
                tup = heapq.heappop(nodePriorityQueue)
            dist, currentNodeIndex = tup
            nodeIndexSet.remove(currentNodeIndex)
            for child in self.graph.nodeArray[currentNodeIndex].children:
                childIndex = child.index
                if childIndex in nodeIndexSet:
                    currentDistance = nodeDist[currentNodeIndex] + getWeight(currentNodeIndex, childIndex)
                    if currentDistance < nodeDist[childIndex]:
                        nodeDist[childIndex] = currentDistance
                        invalidTuples.add((nodeDist[childIndex], childIndex))
                        heapq.heappush(nodePriorityQueue,(currentDistance, childIndex))
                        nodePrev[childIndex] = currentNodeIndex
        
        shortestDistance = nodeDist[targetIndex]
        shortestPath = []
        current = targetIndex

        while current != sourceIndex:
            shortestPath = [current] + shortestPath
            current = nodePrev[current]
        shortestPath = [current] + shortestPath

        return shortestDistance, shortestPath