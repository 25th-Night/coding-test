def check(num):
    if num == 1 or int(num**0.5) == num**0.5:
        return -1
    return 1

def solution(left, right):
    cnt = 0
    for num in range(left, right+1):
        cnt += num * check(num)
    return cnt