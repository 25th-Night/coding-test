from collections import defaultdict

def solution(survey, choices):
    types = ["RT", "CF", "JM", "AN"]
    check = defaultdict(int)
    for s , c in zip(survey, choices):
        if c < 4:
            check[s[0]] += 4 - c
        elif c > 4:
            check[s[1]] += c - 4
    result = ""
    for type_ in types:
        a, b = type_[0], type_[1]
        if check[a] >= check[b]:
            result += a
        else:
            result += b
    return result