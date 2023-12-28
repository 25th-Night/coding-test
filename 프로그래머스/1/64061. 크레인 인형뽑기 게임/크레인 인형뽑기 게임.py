def solution(board, moves):
    n = len(board)
    maps = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            maps[r][c] = board[c][r]
    stack = []
    cnt = 0
    for m in moves:
        for i, c in enumerate(maps[m-1]):
            if c:
                print(c)
                if stack and stack[-1] == c:
                    stack.pop()
                    cnt += 1
                else:
                    stack.append(c)
                maps[m-1][i] = 0
                break
    return cnt * 2