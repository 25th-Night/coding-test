def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2  

    if start in [0, 12 * 3600]:
        answer += 1

    while start < end:
        curr_h = start / 120 % 360
        curr_m = start / 10 % 360
        curr_s = start * 6 % 360

        next_h = (start + 1) / 120 % 360 == 0 and 360 or (start + 1) / 120 % 360
        next_m = (start + 1) / 10 % 360 == 0 and 360 or (start + 1) / 10 % 360
        next_s = (start + 1) * 6 % 360 == 0 and 360 or (start + 1) * 6 % 360

        if curr_s < curr_h and next_s >= next_h:
            answer += 1
        if curr_s < curr_m and next_s >= next_m:
            answer += 1
        if next_s == next_m == next_h:
            answer -= 1

        start += 1
    
    return answer