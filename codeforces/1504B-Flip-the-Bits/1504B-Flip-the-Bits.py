for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    ones = zeros = 0
    legal = [False] * n
    
    for i in range(n):
        if a[i] == "0":
            zeros += 1
        else:
            ones += 1

        if ones == zeros:
            legal[i] = True

    flip = False

    for i in range(n - 1, -1, -1):
        if flip:
            a[i] = "1" if a[i] == "0" else "0"

        if a[i] == b[i]:
            continue

        if not legal[i]:
            print("NO")
            break

        flip = not flip

    else:
        print("YES")