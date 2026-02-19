for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [(list(map(int, input().split()))) for _ in range(n)]
    arr.sort()

    for num in arr:
        i, j, r = num
        if i <= k and k <= r:
            k = r

    print(k)
