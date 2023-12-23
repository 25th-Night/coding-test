def calc(info, x, y):
    if x < 1 or y < 1:
        return 0
    elif (x, y) in info:
        return info[(x, y)]
    else:
        return info.setdefault((x, y), calc(info, x-1, y) + calc(info, x, y-1))

def solution(m, n, puddles):
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for x, y in puddles:
        info[(x, y)] = 0
    return calc(info, m, n) % 1000000007