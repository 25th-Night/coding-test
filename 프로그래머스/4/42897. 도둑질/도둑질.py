def solution(money):
    x1, y1, z1 = money[0], money[1], money[0] + money[2]
    x2, y2, z2 = 0, money[1], money[2]
    for m in money[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1) + m
        x2, y2, z2 = y2, z2, max(x2, y2) + m
    return max(x1, y1, y2, z2)