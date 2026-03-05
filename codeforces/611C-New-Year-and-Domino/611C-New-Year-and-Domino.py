h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
horizontal = [[0] * w for _ in range(h)]
n = int(input())
q = [list(map(int, input().split())) for _ in range(n)]

horizontal = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w - 1):
        if grid[i][j] == "." and grid[i][j + 1] == ".":
            horizontal[i][j] += 1

hprefix = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        hprefix[i][j] = (
            hprefix[i - 1][j]
            + hprefix[i][j - 1]
            - hprefix[i - 1][j - 1]
            + horizontal[i - 1][j - 1]
        )

vertical = [[0] * w for _ in range(h)]

for i in range(h - 1):
    for j in range(w):
        if grid[i][j] == "." and grid[i + 1][j] == ".":
            vertical[i][j] = 1

vprefix = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        vprefix[i][j] = (
            vprefix[i - 1][j]
            + vprefix[i][j - 1]
            - vprefix[i - 1][j - 1]
            + vertical[i - 1][j - 1]
        )

for r1, c1, r2, c2 in q:
    ph = (
        hprefix[r2][c2 - 1]
        - hprefix[r2][c1 - 1]
        - hprefix[r1 - 1][c2 - 1]
        + hprefix[r1 - 1][c1 - 1]
    )
    pv = (
        vprefix[r2 - 1][c2]
        - vprefix[r1 - 1][c2]
        - vprefix[r2 - 1][c1 - 1]
        + vprefix[r1 - 1][c1 - 1]
    )
    print(ph + pv)