from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    if 'a' not in s:
        print(-1)
        continue

    answer = float('inf')
    a_indices = [i for i in range(n) if s[i] == 'a']

    for i in range(len(a_indices)):
        for j in range(i + 1, len(a_indices)):
            length = a_indices[j] - a_indices[i] + 1
            if length > 7:
                break

            sub = s[a_indices[i]:a_indices[j] + 1]
            cnt = Counter(sub)

            if cnt['a'] > cnt['b'] and cnt['a'] > cnt['c']:
                answer = min(answer, length)
                break

    print(-1 if answer == float('inf') else answer)
