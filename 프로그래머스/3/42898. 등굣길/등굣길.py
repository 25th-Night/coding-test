def solution(m, n, puddles):
    puddles = [[r-1, c-1] for r, c in puddles]
    maps = [[1] * m for _ in range(n)]
    for c, r in puddles:
        if not r:
            for i in range(c, m):
                maps[r][i] = 0
        elif not c:
            for i in range(r, n):
                maps[i][c] = 0
        else:
            maps[r][c] = 0
    for i in range(1, n):
        for j in range(1, m):
            maps[i][j] = maps[i][j-1] + maps[i-1][j] if maps[i][j] else 0
                
    return maps[-1][-1] % 1000000007