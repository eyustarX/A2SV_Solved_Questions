class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        state = defaultdict(list)
        outdegree = [0] * n
        
        for i in range(n):
            outdegree[i] = len(graph[i])
            for j in graph[i]:
                state[j].append(i)
        print(state)
        queue = deque()
        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)
        
        safe_state = []

        while queue:
            node = queue.popleft()
            safe_state.append(node)

            for n in state[node]:
                outdegree[n] -= 1
                if outdegree[n] == 0:
                    queue.append(n)
        
        return sorted(safe_state)