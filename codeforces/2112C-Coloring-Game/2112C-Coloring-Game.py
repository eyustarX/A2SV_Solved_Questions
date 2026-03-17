t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, n):
        max_value = max(arr[i], arr[-1] - arr[i])

        j = 0
        k = i - 1

        while j < k:
            if arr[j] + arr[k] > max_value:
                ans += k - j
                k -= 1
            else:
                j += 1

    print(ans)