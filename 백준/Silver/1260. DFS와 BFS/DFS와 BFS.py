import sys
from copy import deepcopy

def make_graph(cds):
    graph = [[] for _ in range(N+1)]
    for x, y in cds:
        graph[x].append(y)
        graph[y].append(x)
    for row in graph:
        row.sort()
    return graph

def bfs(graph, visited, start):
    q = [start]
    result = []
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = True
            result.append(v)
            for n in graph[v]:
                if not visited[n]:
                    q.append(n)
    return result

def dfs(graph, visited, start):
    stack = [start]
    result = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            result.append(v)
            graph[v].sort(reverse=True)
            for n in graph[v]:
                if not visited[n]:
                    stack.append(n)
    return result

input = sys.stdin.readline


N, M, V = map(int, input().split())
cds = [tuple(map(int, input().split())) for _ in range(M)]

visited = [False] * (N+1)
graph = make_graph(cds)

print(*dfs(deepcopy(graph), visited.copy(), V))
print(*bfs(deepcopy(graph), visited.copy(), V))
      