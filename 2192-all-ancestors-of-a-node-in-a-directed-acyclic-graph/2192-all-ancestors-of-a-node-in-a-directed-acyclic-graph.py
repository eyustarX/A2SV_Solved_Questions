class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n

        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1

        ans = [set() for _ in range(n)]
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()

            for n in graph[node]:
                ans[n].add(node)
                ans[n].update(ans[node])

                indegree[n] -= 1

                if indegree[n] == 0:
                    queue.append(n)
        
        return [sorted(i) for i in ans]

