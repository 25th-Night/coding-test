from collections import defaultdict

def solution(genres, plays):
    total = defaultdict(int)
    for g, p in zip(genres, plays):
        total[g] += p

    info = []
    for i, (g, p) in enumerate(zip(genres, plays)):
        info.append([g, total[g], p, i])

    info.sort(key=lambda x:(-x[1], -x[2], x[3]))

    check = defaultdict(int)
    result = []
    for g, t, p, i in info:
        if check[g] < 2:
            result.append(i)
            check[g] += 1
    return result