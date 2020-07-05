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
    
    def dfs_recurse(self):
        pass

    def dfs_iterative(self):
        pass

    def bfs(self):
        pass