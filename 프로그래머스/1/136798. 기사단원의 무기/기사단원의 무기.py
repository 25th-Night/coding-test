def cnt_divisor(num):
    cnt = 0
    if num**0.5 == int(num**0.5):
        cnt -= 1
    for i in range(1, int(num**0.5)+1):
        if not num%i:
            cnt += 2
    return cnt


def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        answer += cnt_divisor(num) if cnt_divisor(num) <= limit else power
    return answer