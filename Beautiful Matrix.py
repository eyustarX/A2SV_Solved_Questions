matrix = []
row, column = 0, 0
 
for i in range(5):
    n = list(map(int, input().split()))
    matrix.append(n)
    if 1 in n:
        row = i
        column = n.index(1)
 
 
count = abs(2 - row) + abs(2 - column)
print(count)
