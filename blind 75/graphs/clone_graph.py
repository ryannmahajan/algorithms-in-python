
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        graph = {}

        def dfs(curr):
            if not curr: return None
            clone = graph.get(curr.val, Node(curr.val))

            if curr.val not in graph:
                graph[curr.val] = clone

                for neighbour in curr.neighbors:
                    clone_neighbour = dfs(neighbour)

                    clone.neighbors.append(clone_neighbour)
                    # clone_neighbour.neighbors.append(clone)

            return clone
        
        return dfs(node)

        
