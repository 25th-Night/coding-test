cnt = int(input())
ps = int(input())

graph = [[] for _ in range(cnt+1)]

for _ in range(ps):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (cnt+1)

connect = 0
q = [1]
while q:
    v = q.pop(0)
    if not visited[v]:
        visited[v] = True
        connect += 1
        for n in graph[v]:
            if not visited[n]:
                q.append(n)

print(connect-1)