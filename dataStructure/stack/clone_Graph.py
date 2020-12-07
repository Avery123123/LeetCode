class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        new = Node(node.val, [])
        visited = {node:new}
        self.DFS(visited, node)
        return new
        
    def DFS(self, visited, node):
        for i in node.neighbors:
            if i not in visited:
                visited[i] = Node(i.val, [])
                self.DFS(visited, i)
            visited[node].neighbors.append(visited[i])


