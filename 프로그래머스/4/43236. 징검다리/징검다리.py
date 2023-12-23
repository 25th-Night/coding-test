def solution(distance, rocks, n):
    answer = 0
    s, e = 0, distance
    rocks.sort()
    rocks.append(distance)
    while s <= e:
        m = (s + e) // 2
        cnt = 0
        curr = 0
        for r in rocks:
            dist = r - curr
            if dist < m:
                cnt += 1
            else:
                curr = r
        if cnt > n:
            e = m - 1
        else:
            s = m + 1
            answer = m
    return answer