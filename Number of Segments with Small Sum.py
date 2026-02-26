n, s = map(int, input().split())
a = list(map(int, input().split()))

window_sum = 0
l = 0
count = 0

for r in range(n):
    window_sum += a[r]

    while window_sum > s:
        window_sum -= a[l]
        l += 1

    count += r - l + 1
print(count)
