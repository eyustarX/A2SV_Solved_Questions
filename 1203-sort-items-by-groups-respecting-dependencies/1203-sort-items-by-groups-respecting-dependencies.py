class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])

        for g in group_graph:
            unique = set(group_graph[g])
            group_graph[g] = list(unique)
        for g in group_graph:
            for nei in group_graph[g]:
                group_indegree[nei] += 1

        def topo_sort(graph, indegree, size):
            queue = deque()
            for i in range(size):
                if indegree[i] == 0:
                    queue.append(i)

            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

            return order if len(order) == size else []

        group_order = topo_sort(group_graph, group_indegree, group_id)
        if not group_order:
            return []

        item_order = topo_sort(item_graph, item_indegree, n)
        if not item_order:
            return []

        grouped_items = defaultdict(list)
        for item in item_order:
            grouped_items[group[item]].append(item)

        result = []
        for g in group_order:
            result.extend(grouped_items[g])

        return result