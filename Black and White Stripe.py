from collections import Counter as c

for _ in range(int(input())):
    n, k = map(int, input().split())
    stripe = input().strip()

    window = c(stripe[:k])
    ans = window["B"]

    for i in range(n - k):
        window[stripe[i]] -= 1
        window[stripe[i + k]] += 1
        ans = max(ans, window["B"])

    print(k - ans)
