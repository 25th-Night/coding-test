from collections import defaultdict

def make_graph(edge):
    graph = defaultdict(list)
    [graph[a].append(b) == graph[b].append(a) for a, b in edge]
    return graph

def bfs(graph, visited, dist, start):
    q = [start]
    while q:
        v = q.pop(0)
        visited[v] = True
        for n in graph[v]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                dist[n] = dist[v] + 1

def solution(n, edge):
    graph = make_graph(edge)
    visited = [False] * (n+1)
    dist = [0] * (n+1)
    bfs(graph, visited, dist, 1)
    return dist.count(max(dist))