n, s = map(int, input().split())
a = list(map(int, input().split()))

window_sum = 0
l = 0
count = 0

for i in range(n):
    window_sum += a[i]
    while window_sum >= s:
        count += n - i
        window_sum -= a[l]
        l += 1

print(count)
