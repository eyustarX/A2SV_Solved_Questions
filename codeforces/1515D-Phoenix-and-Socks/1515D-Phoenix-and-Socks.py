from collections import Counter

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    lcount = Counter(a[:l])
    rcount = Counter(a[l:n])

    for i in lcount.keys() & rcount.keys():
        mini = min(lcount[i], rcount[i])
        lcount[i] -= mini
        rcount[i] -= mini
        l -= mini
        r -= mini

        if lcount[i] == 0:
            del lcount[i]
        if rcount[i] == 0:
            del rcount[i]
    if l < r:
        lcount, rcount = rcount, lcount
        l, r = r, l

    ans = 0

    for key in lcount:
        extra = l - r
        pair = lcount[key] // 2
        swap = min(pair * 2, extra)

        ans += swap // 2
        l -= swap

    ans += (l - r) // 2 + (l + r) // 2

    print(ans)