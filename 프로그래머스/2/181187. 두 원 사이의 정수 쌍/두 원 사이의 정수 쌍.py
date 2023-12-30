from math import ceil

def solution(r1, r2):
    answer = r2 - r1 + 1
    for i in range(1, r2):
        if i < r1:
            answer += int((r2**2 - i**2)**0.5) - ceil((r1**2 - i**2)**0.5) + 1
        elif i >= r1:
            answer += int((r2**2 - i**2)**0.5)
    return answer * 4