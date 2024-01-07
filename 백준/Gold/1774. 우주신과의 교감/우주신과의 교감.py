import sys

def get_distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return (x**2 + y**2)**0.5

def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = get_parent(parent, x)
    b = get_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_paren(parent, x, y):
    a = get_parent(parent, x)
    b = get_parent(parent, y)
    return a == b

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
parent = list(range(n+1))
locations = []

for _ in range(n):
    x, y, = map(int, input().split())
    locations.append((x, y))

length = len(locations)

for i in range(length - 1):
    for j in range(i+1, length):
        edges.append((i+1, j+1, get_distance(locations[i], locations[j])))

for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

edges.sort(key=lambda x:x[2])

result = 0
for a, b, cost in edges:
    if not find_paren(parent, a, b):
        union_parent(parent, a, b)
        result += cost

print(f"{result:.2f}")