class TreeAdjacencyList:
    def __init__(self, adjacencyList, **kwarg):
        """
        adjacencyList should be of the form:
        adjacencyList = {0: [1,2], 1: [None, None], 2: [None, 3], 3: [None, None]}
        kwarg can be any arbitrary attributes to add to the nodes.
        Should be of the form: color = {0: 'red', 1: 'blue', 2: 'green'}
        Keys are the node indices.
        Node with index 0 will be the tree root.
        """
        self.adjacencyList = adjacencyList
        self.attrDict = None
        if kwarg:
            self.attrDict = kwarg

class BinaryTree:
    class _Node:
        def __init__(self, index, value = None, attrDict = None):
            self.index = index
            self.value = value
            self.attr = {}
            if attrDict is not None:
                self.attr = attrDict
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
    
    def buildFromAdjacencyList(self, graphAdjacencyList):
        adjacencyList = graphAdjacencyList.adjacencyList
        attrDict = graphAdjacencyList.attrDict
        # Create nodes
        self.nodeArray = [self._Node(index) for index in adjacencyList]
        self.root = self.nodeArray[0] # Root is always node with 0 index
        # Link nodes
        for index, links in adjacencyList.items():
            node = self.nodeArray[index]
            leftLink, rightLink = links
            if leftLink:
                leftChild = self.nodeArray[leftLink]
                node.left = leftChild
            if rightLink:
                rightChild = self.nodeArray[rightLink]
                node.right = rightChild
        # Add node attributes
        if attrDict:
            for attrName, attrList in attrDict.items():
                if attrName.lower() in ['values', 'value', 'vals']:
                    for index, value in attrList.items():
                        node = self.nodeArray[index]
                        node.value = value
                else:
                    for index, content in attrList.items():
                        node = self.nodeArray[index]
                        node.attr[attrName] = content
