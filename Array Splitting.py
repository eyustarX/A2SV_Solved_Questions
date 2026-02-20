n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(a[-1] - a[0])
    
else:
    gaps = []
    for i in range(1, n):
        gaps.append(a[i] - a[i - 1])

    gaps.sort(reverse=True)
    total = a[-1] - a[0]

    print(total - sum(gaps[: k - 1]))
