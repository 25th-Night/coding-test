import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

def dfs(graph, visited, s):
    visited[s] = True
    for n in graph[s]:
        if not visited[n]:
            visited[n] = True
            dist[n] = dist[s] + graph[s][n]
            dfs(graph, visited, n)


N, M = map(int, input().split())
graph = defaultdict(dict)
for _ in range(N-1):
    x, y, d = map(int, input().split())
    graph[x][y]=d
    graph[y][x]=d
result = [0]* M

for i in range(M):
    s, e = map(int, input().split())
    visited= [False] * (N+1)
    dist = [0] * (N+1)
    dfs(graph, visited, s)
    print(dist[e])
