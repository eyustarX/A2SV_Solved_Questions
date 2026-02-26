n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
i = j = 0

while i < n and j < m:
    if a[i] == b[j]:
        l = r = 1
        while i + l < n and a[i] == a[i + l]:
            l += 1
        while j + r < m and b[j] == b[j + r]:
            r += 1
        i += l
        j += r
        count += r * l
    elif a[i] > b[j]:
        j += 1
    else:
        i += 1

print(count)
