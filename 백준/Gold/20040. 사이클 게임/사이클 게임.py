import sys

input = sys.stdin.readline

def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a, b = get_parent(parent, x), get_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = list(range(n))
result = 0

for i in range(m):
    x, y = map(int, input().split())
    if get_parent(parent, x) != get_parent(parent, y):
        union_parent(parent, x, y)
    else:
        result = i + 1
        break

print(result)