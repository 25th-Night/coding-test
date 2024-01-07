import sys
from collections import deque

input = sys.stdin.readline

def bfs(r, c):
    q = deque([(r, c)])
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        cr, cc = q.popleft()

        for r, c in move:
            nr, nc = cr+r, cc+c

            if nr in range(len(graph)) and nc in range(len(graph[0])) and graph[nr][nc]:
                q.append((nr, nc))
                graph[nr][nc] = 0
    return 1


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        c, r = map(int, input().split())
        graph[r][c] = 1

    cnt = 0
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 1:
                cnt += bfs(r, c)

    print(cnt)