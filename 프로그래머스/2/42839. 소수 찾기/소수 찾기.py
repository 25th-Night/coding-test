from itertools import permutations

def check_prime(num):
    if num < 4:
        return num // 2
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return 0
    return 1

def solution(numbers):
    result = 0
    for i in range(1, len(numbers) + 1):
        for x in set(permutations(list(numbers), i)):
            if x[0] != "0":
                num = int("".join(x))
                result += check_prime(num)
    return result