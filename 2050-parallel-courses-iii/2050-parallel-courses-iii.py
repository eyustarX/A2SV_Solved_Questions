class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n

        for u,v in relations:
            graph[u - 1].append(v - 1)
            indegree[v - 1] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        ans = time[:]

        while queue:
            node = queue.popleft()

            for ne in graph[node]:
                ans[ne] = max(ans[ne],ans[node] + time[ne])
                
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    queue.append(ne)
        

        return max(ans)