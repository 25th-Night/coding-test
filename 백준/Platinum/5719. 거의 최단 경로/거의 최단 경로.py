import sys
from heapq import heappop, heappush
from collections import deque

input = sys.stdin.readline

def dijkstra(graph, dropped, start):
    dist = [1e9 for _ in range(n)]
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cd, cn = heappop(heap)

        if dist[cn] >= cd:
            for nd, nn in graph[cn]:
                d = cd + nd
                if dist[nn] > d and not dropped[cn][nn]:
                    dist[nn] = d
                    heappush(heap, (d, nn))

    return dist

def bfs(rev_g, dropped, start, end):
    queue = deque()
    queue.append(end)

    while queue:
        cn = queue.popleft()

        if cn != start:
            for pd, pn in rev_g[cn]:
                if dist[pn] + pd == dist[cn] and not dropped[pn][cn]:
                    dropped[pn][cn] = True
                    queue.append(pn)

while True:
    n, m = map(int, input().split())
    if not n:
        break
    graph = [[] for _ in range(n)]
    rev_g = [[] for _ in range(n)]
    dropped = [[False] * n for _ in range(n)]
    start, end = map(int, input().split())

    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((p, v))
        rev_g[v].append((p, u))

    dist = dijkstra(graph, dropped, start)
    bfs(rev_g, dropped, start, end)
    dist = dijkstra(graph, dropped, start)

    print(dist[end] if dist[end] != 1e9 else -1)