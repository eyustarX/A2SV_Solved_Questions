from collections import defaultdict as d

n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
hash_map = d(int)
left = 0
l = r = 0
for right in range(n):
    hash_map[a[right]] += 1

    while len(hash_map) > k:
        hash_map[a[left]] -= 1
        if hash_map[a[left]] == 0:
            del hash_map[a[left]]
        left += 1
    new_max = right - left + 1
    if new_max > count:
        l = left
        r = right
        count = new_max

print(l + 1, r + 1)
