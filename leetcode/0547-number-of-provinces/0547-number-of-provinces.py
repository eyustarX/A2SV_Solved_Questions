from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)

            if rx != ry:
                if size[rx] > size[ry]:
                    parent[ry] = rx
                    size[rx] += size[ry]
                else:
                    parent[rx] = ry
                    size[ry] += size[rx]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        provinces = set()
        for i in range(n):
            provinces.add(find(i))

        return len(provinces)