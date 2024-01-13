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

N, M = map(int, input().split())

parent = list(range(N+1))

for _ in range(M):
    x, y, = map(int, input().split())
    if get_parent(parent, x) != get_parent(parent, y):
        union_parent(parent, x, y)

counter = set()
for i in range(1, N+1):
    counter.add(get_parent(parent, i))

print(len(counter))