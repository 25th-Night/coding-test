def solution(board, ch, cw):
    answer = 0
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = len(board)
    for h, w in move:
        nh, nw = ch + h, cw + w
        if nh in range(n) and nw in range(n) and \
            board[nh][nw] == board[ch][cw]:
            answer += 1
    return answer