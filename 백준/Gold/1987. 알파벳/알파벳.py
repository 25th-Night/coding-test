R, C = map(int, input().split())
maps = [input() for _ in range(R)]
visited = [False] * 26
visited[ord(maps[0][0]) - ord("A")] = True

def dfs(maps, visited, cr, cc, cnt):
    global length
    length = max(length, cnt)
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for r, c in move:
        nr, nc = cr+r, cc+c
        if nr in range(len(maps)) and nc in range(len(maps[0])) and not visited[ord(maps[nr][nc]) - ord("A")]:
            visited[ord(maps[nr][nc]) - ord("A")] = 1
            dfs(maps, visited, nr, nc, cnt+1)
            visited[ord(maps[nr][nc]) - ord("A")] = 0
            
length = 0
dfs(maps, visited, 0, 0, 1)

print(length)