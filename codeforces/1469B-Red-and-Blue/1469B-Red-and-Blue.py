for _ in range(int(input())):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))

    for i in range(1, n):
        red[i] += red[i - 1]

    for i in range(1, m):
        blue[i] += blue[i - 1]

    r = max(red)
    b = max(blue)
    ans = r + b
    
    if r < 0 and b >= 0:
        ans = b
    elif r >= 0 and b < 0:
        ans = r
    print(ans if ans >= 0 else 0)