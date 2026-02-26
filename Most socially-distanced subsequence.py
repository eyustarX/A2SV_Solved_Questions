for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    subs = []
    l = 0

    while l < n - 1:
        subs.append(s[l])
        r = l + 1
        if s[l] > s[r]:
            while r < n - 1 and s[r] >= s[r + 1]:
                r += 1

        else:
            while r < n - 1 and s[r] < s[r + 1]:
                r += 1

        l = r
    subs.append(s[-1])

    print(len(subs))
    print(*subs)
