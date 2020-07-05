class GraphAdjacencyList:
    def __init__(self, adjacencyList, **kwarg):
        self.adjacencyList = adjacencyList
        self.attrDict = None
        if kwarg:
            self.attrDict = kwarg

class Graph:
    """
    This class deals with the graph internal data representation.
    CUD operations live here.
    Anything to do with reading graph data and analysing it is implemented in the GraphAlgos class.
    """
    class _Node:
        def __init__(self, index, value = None, attrDict = None):
            self.index = index
            self.value = value
            self.attr = {}
            if attrDict is not None:
                self.attr = attrDict
            self.children = []

    def __init__(self):
        self.nodeArray = None

    def buildFromAdjacencyList(self, graphAdjacencyList):
        adjacencyList = graphAdjacencyList.adjacencyList
        attrDict = graphAdjacencyList.attrDict
        # Create nodes
        self.nodeArray = [self._Node(index) for index in adjacencyList]
        # Link nodes
        for index, links in adjacencyList.items():
            node = self.nodeArray[index]
            for link_index in links:
                link_node = self.nodeArray[link_index]
                node.children.append(link_node)
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


