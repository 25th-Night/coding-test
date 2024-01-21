from collections import deque
from copy import deepcopy

def bfs(maps, sr, sc, T):
    q = deque([(sr, sc)])
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        cr, cc = q.popleft()
        maps[cr][cc] = 0
        for r, c in move:
            nr, nc = cr+r, cc+c
            if nr in range(len(maps)) and nc in range(len(maps[0])) and maps[nr][nc] == T:
                q.append((nr, nc))
                maps[nr][nc] = 0
    return 1

N = int(input())
maps = [list(input()) for _ in range(N)]
maps2 = deepcopy(maps)
for i in range(len(maps2)):
    for j in range(len(maps2[0])):
        if maps2[i][j] == "G":
            maps2[i][j] = "R"

result1, result2 = 0, 0
for r in range(N):
    for c in range(N):
        if maps[r][c]:
            result1 += bfs(maps, r, c, maps[r][c])
        if maps2[r][c]:
            result2 += bfs(maps2, r, c, maps2[r][c])

print(result1, result2)