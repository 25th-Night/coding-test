import sys
from heapq import heappop, heappush

def dijkstra(graph, times, start):
    heap = []
    heappush(heap, (0, start))
    times[start] = 0
    while heap:
        ct, cn = heappop(heap)
        if times[cn] >= ct:
            for nn, nt in graph[cn]:
                time = ct + nt
                if times[nn] > time:
                    times[nn] = ct + nt
                    heappush(heap, (time, nn))

# input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    times = [1e9] * (n+1)
    for _ in range(m):
        x, y, time = map(int, input().split())
        graph[y].append((x, time))
    dijkstra(graph, times, c)
    cnt = 0
    max_time = 0
    for t in times:
        if t != 1e9:
            cnt += 1
            if t > max_time:
                max_time = t

    print(cnt, max_time)