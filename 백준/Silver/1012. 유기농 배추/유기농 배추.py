import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph):
    cnt = 0
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if graph[r][c] == 1:
                cnt += 1
                q = deque([(r, c)])
                move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                while q:
                    cr, cc = q.popleft()

                    for dr, dc in move:
                        nr, nc = cr + dr, cc + dc

                        if nr in range(len(graph)) and nc in range(len(graph[0])) and graph[nr][nc]:
                            q.append((nr, nc))
                            graph[nr][nc] = 0
    return cnt


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for i in range(k):
        c, r = map(int, input().split())
        graph[r][c] = 1

    print(bfs(graph))