from bisect import bisect_left

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    flag = True
    prev = float("-inf")
    for num in a:
        best = float("inf")

        if num >= prev:
            best = num
        j = bisect_left(b, prev + num)
        if j < m:
            val = b[j] - num
            if val >= prev:
                best = min(best, val)

        if best == float("inf"):
            flag = False
            break

        prev = best

    if flag:
        print("YES")
    else:
        print("NO")