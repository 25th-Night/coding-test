from itertools import combinations

def check(num):
    for n in range(2, int(num**0.5)+1):
        if not num%n:
            return False
    return True

def solution(nums):
    arr = list(map(sum, combinations(nums, 3)))
    return len(list(filter(lambda x:check(x)==True, arr)))