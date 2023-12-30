def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for v in lst:
            if v[0] > x[1]:
                v[0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))