def solution(d, budget):
    d.sort()
    for idx, cost in enumerate(d):
        budget -= cost
        if budget < 0:
            return idx
    return idx+1