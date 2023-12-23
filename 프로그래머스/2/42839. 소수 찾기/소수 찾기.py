from itertools import permutations

def check_prime(num):
    if num // 2 == 1:
        return 1
    elif not num // 2 or not num % 2:
        return 0
    else:
        for n in range(3, int(num**0.5)+1):
            if not num % n:
                return 0
        return 1

def solution(numbers):
    cnt = 0
    nums = set()
    for i in range(1, len(numbers)+1):
        nums |= set(map(lambda x: int("".join(x)), permutations(numbers, i)))
    for num in nums:
        cnt += check_prime(num)
    return cnt