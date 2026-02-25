for _ in range(int(input())):
    s = input()
    l = 0
    res = set()

    while l < len(s):
        r = l

        while r < len(s) and s[r] == s[l]:
            r += 1

        if (r - l) % 2 == 1:
            res.add(s[l])

        l = r

    print("".join(sorted(res)))
