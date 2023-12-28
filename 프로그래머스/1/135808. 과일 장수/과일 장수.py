def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    box = []
    for s in score:
        if len(box) < m:
            box.append(s)
            if len(box) == m:
                answer += min(box) * m
                box = []
    return answer