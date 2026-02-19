t = int(input())
arr = list(map(int, input().split()))
arr.sort()

i = 1
count = 0

for num in arr:
    if i <= num:
        count += 1
        i += 1

print(count)
