from collections import deque, defaultdict

def bfs(maps, visited, r, c):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cnt = 1
    max_c, min_c = c, c
    q = deque([(r, c)])
    visited[r][c] = True
    while q:
        cr, cc = q.popleft()
        for r, c in move:
            nr, nc = cr+r, cc+c
            if nr in range(len(maps)) and nc in range(len(maps[0])) and not visited[nr][nc] and maps[nr][nc] == 1:
                max_c, min_c = max(max_c, nc), min(min_c, nc)
                cnt += 1
                q.append((nr, nc))
                visited[nr][nc] = True
    
    return cnt, max_c, min_c

def solution(land):
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    dp = [0] * len(land[0])
    for r in range(len(land)):
        for c in range(len(land[0])):
            if land[r][c] == 1 and not visited[r][c]:
                cnt, max_c, min_c = bfs(land, visited, r, c)
                for i in range(min_c, max_c+1):
                    dp[i] += cnt
    return max(dp)