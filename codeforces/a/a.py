from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, start):
    depth = [-1] * (n + 1)
    q = deque([start])
    depth[start] = 0
    far = start

    while q:
        node = q.popleft()
        for nei in graph[node]:
            if depth[nei] == -1:
                depth[nei] = depth[node] + 1
                if depth[nei] > depth[far]:
                    far = nei
                q.append(nei)

    return far, depth


a, b = bfs(graph, 1)
_, depth = bfs(graph, a)

print(max(depth) * 3)