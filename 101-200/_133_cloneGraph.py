# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        def dfs(node_):
            pass

        def bfs(node_):
            pass

        node_table = {}

        node = dfs(node)
        node = bfs(node)
        return node
