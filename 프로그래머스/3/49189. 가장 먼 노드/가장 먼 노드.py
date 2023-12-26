from collections import defaultdict

def make(edge):
    g = defaultdict(list)
    for a, b in edge:
        g[a].append(b)
        g[b].append(a)
    return g

def bfs(graph, visited, dist, start):
    q= [start]
    while q:
        v = q.pop(0)
        visited[v] = True
        for n in graph[v]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                dist[n] = dist[v] + 1

def solution(n, edge):
    visited = [False] * (n+1)
    graph = make(edge)
    dist = [0] * (n+1)
    bfs(graph, visited, dist, 1)
    return dist.count(max(dist))