from collections import defaultdict

def solution(players, callings):
    rank = defaultdict(str)
    check = defaultdict(int)
    for i, p in enumerate(players, 1):
        rank[i] = p
        check[p] = i
    for p in callings:
        c_rank = check[p]
        ap = rank[c_rank-1]
        rank[c_rank-1], rank[c_rank] = p, ap
        check[p], check[ap] = c_rank-1, c_rank
    
    return list(rank.values())