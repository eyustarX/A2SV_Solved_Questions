def backtracking(i, current):
    global count, total
    if i == len(s2):
        if current == target:
            count += 1
        total += 1
        return
    if s2[i] == "+":
        backtracking(i + 1, current + 1)
    elif s2[i] == "-":
        backtracking(i + 1, current - 1)
    else:
        backtracking(i + 1, current + 1)
        backtracking(i + 1, current - 1)


backtracking(0, 0)

print(count / total)