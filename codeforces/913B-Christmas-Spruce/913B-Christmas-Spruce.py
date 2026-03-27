from collections import defaultdict

tree = defaultdict(list)
n = int(input())

for i in range(2, n + 1):
    tree[int(input())].append(i)

for key in tree.keys():
    for num in tree[key][:]:
        if num in tree:
            tree[key].remove(num)

    if len(tree[key]) < 3:
        print("No")
        break

else:
    print("Yes")