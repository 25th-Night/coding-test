def solution(money):
    # 첫 집을 무조건 터는 경우
    x1, y1, z1 = money[0], money[1], money[0] + money[2]
    # 마지막 집을 무조건 터는 경우
    x2, y2, z2 = 0, money[1], money[2]
    
    for m in money[3:]:
        # 다음 집들 털면서 업데이트
        x1, y1, z1 = y1, z1, max(x1, y1) + m
        x2, y2, z2 = y2, z2, max(x2, y2) + m
    return max(x1, y1, y2, z2)