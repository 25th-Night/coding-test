N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]
rs, cs = [0] * N, [0] * M

for r in range(N):
    for c in range(M):
        if maps[r][c] == "X":
            rs[r] = 1
            cs[c] = 1

print(max(N-sum(rs), M-sum(cs)))