from collections import defaultdict

def solution(s):
    check = defaultdict(int)
    answer = []
    for i, c in enumerate(s):
        if c not in check:
            answer.append(-1)
        else:
            answer.append(i-check[c])
        check[c] = i
    return answer