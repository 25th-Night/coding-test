def solution(n, m, section):
    cnt = 1
    curr = section[0]
    for s in section[1:]:
        if s > curr + m - 1:
            curr = s
            cnt += 1
    return cnt
        