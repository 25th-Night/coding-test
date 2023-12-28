from collections import Counter

def solution(X, Y):
    check = Counter(X) & Counter(Y)
    if not check:
        return "-1"
    elif set(check.keys()) == {"0"}:
        return "0"
    else:
        result = []
        for k in check:
            result.append(k*check[k])
        result.sort(reverse=True)
        return "".join(result)