import heapq

heap = []
ans = []

n = int(input())

for _ in range(n):

    s = input().split()

    if s[0] == "insert":

        x = int(s[1])

        heapq.heappush(heap, x)
        ans.append(f"insert {x}")

    elif s[0] == "removeMin":

        if not heap:
            heapq.heappush(heap, 0)
            ans.append("insert 0")

        heapq.heappop(heap)
        ans.append("removeMin")

    else:

        x = int(s[1])

        while heap and heap[0] < x:
            heapq.heappop(heap)
            ans.append("removeMin")

        if not heap or heap[0] > x:
            heapq.heappush(heap, x)
            ans.append(f"insert {x}")

        ans.append(f"getMin {x}")

print(len(ans))

for op in ans:
    print(op)