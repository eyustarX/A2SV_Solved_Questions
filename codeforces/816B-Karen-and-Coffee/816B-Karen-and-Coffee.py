n, k, q = map(int, input().split())
recipe = []
min_v, max_v = 200000, 0

for _ in range(n):
    l, r = map(int, input().split())
    if l < min_v:
        min_v = l
    if r > max_v:
        max_v = r
    recipe.append([l, r])

prefix = [0] * (max_v - min_v + 1)
for l, r in recipe:
    prefix[l - min_v] += 1
    if r != max_v:
        prefix[r - min_v + 1] -= 1

for i in range(1, len(prefix)):
    prefix[i] += prefix[i - 1]

fast_prefix = [1 if x >= k else 0 for x in prefix]
for i in range(1, len(fast_prefix)):
    fast_prefix[i] += fast_prefix[i - 1]

for _ in range(q):
    a, b = map(int, input().split())
    a = max(a, min_v)
    b = min(b, max_v)
    if a > b:
        print(0)
    else:
        ans = fast_prefix[b - min_v]
        if a > min_v:
            ans -= fast_prefix[a - min_v - 1]
        print(ans)