class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = defaultdict(int)

        def dfs(node, color):
            colored[node] = color

            for neighbour in graph[node]:
                if neighbour not in colored:
                    if not dfs(neighbour, 1 - color):
                        return False
                elif colored[neighbour] == color:
                    return False
            
            return True

        for i in range(len(graph)):
            if i not in colored:
                if not dfs(i,0):
                    return False
        
        return True
