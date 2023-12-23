def make_graph(wires, n):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def bfs(graph, visited, start):
    cnt = 0
    q = [start]
    while q:
        v = q.pop(0)
        visited[v] = True
        cnt += 1
        if graph[v]:
            for n in graph[v]:
                if not visited[n]:
                    q.append(n)
    return cnt

from copy import deepcopy

def solution(n, wires):
    result = float("inf")
    for wire in wires:
        visited = [False] * (n+1)
        tmp = deepcopy(wires)
        tmp.remove(wire)
        graph = make_graph(tmp, n)
        cnt = bfs(graph, visited, tmp[0][0])
        result = min(result, abs(n - 2 * cnt))
    return result