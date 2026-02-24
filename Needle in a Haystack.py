for _ in range(int(input())):
    s = list(input())
    t = list(input())

    for i in range(len(s)):
        if s[i] not in t:
            print("Impossible")
            break
        else:
            t.remove(s[i])

    else:
        n = sorted(t)
        ans = []
        left, l = 0, 0
        while left < len(s) and l < len(n):
            if s[left] <= n[l]:
                ans.append(s[left])
                left += 1
            else:
                ans.append(n[l])
                l += 1
        if l != len(n):
            ans.extend(n[l:])
            print("".join(ans))

        else:
            ans.extend(s[left:])
            print("".join(ans))
