from collections import deque

def bfs(board, visited, r, c):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        cr, cc = q.popleft()
        if board[cr][cc] == 'G':
            return visited[cr][cc]
        for r, c in move:
            nr, nc = cr, cc
            while True:
                nr, nc = nr+r, nc+c
                if nr in range(len(board)) and nc in range(len(board[0])) and board[nr][nc]=='D':
                    nr -= r
                    nc -= c
                    break
                elif nr not in range(len(board)) or nc not in range(len(board[0])):
                    nr -= r
                    nc -= c
                    break
            if not visited[nr][nc]:
                visited[nr][nc] = visited[cr][cc] + 1
                q.append((nr, nc))
    return -1

def solution(board):
    answer = 0
    visited = [[0]*len(board[0]) for _ in range(len(board))]
    for r in range(len(board)):
        if "R" in board[r]:
            cr, cc = r, board[r].index("R")
                    
    answer = bfs(board, visited, cr, cc)
    
    if answer > 0:
        answer -= 1
        
    return answer