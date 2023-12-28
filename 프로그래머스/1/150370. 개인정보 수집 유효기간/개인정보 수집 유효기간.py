def solution(today, terms, privacies):
    result = []
    term_info = {}
    for term in terms:
        t, m = term.split(" ")
        term_info[t] = int(m) * 28
    for i, p in enumerate(privacies, 1):
        d, t = p.split(" ")
        y, m, d = map(int, d.split("."))
        ty, tm, td = map(int, today.split("."))
        diff = (ty-y)*12*28 + (tm-m)*28 + (td-d)
        if diff >= term_info[t]:
            result.append(i)
    return result