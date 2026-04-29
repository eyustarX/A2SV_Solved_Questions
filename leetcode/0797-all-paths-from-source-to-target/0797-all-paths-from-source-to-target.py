class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def dfs(node,path):
            path.append(node)
            
            if node == len(graph) - 1:
                ans.append(path[:])
                
            for nei in graph[node]:
                dfs(nei,path)
                path.pop()
            
        dfs(0,[])

        return ans