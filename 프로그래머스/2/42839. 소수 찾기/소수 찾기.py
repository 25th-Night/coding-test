from itertools import permutations

def check_prime_num(num: int):
    if num in [0, 1] or (num > 2 and num % 2 == 0):
        return False
    elif num in [2, 3]:
        return True
    else:
        for i in range(2, int(num**(0.5))+1):
            if num % i == 0:
                return False
        return True
    

def solution(numbers):
    result = set()
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        check_list = permutations(numbers, i)
        check_list = set(map(lambda x: int("".join(x)), check_list))
        for num in check_list:
            if check_prime_num(num):
                result.add(num)
    return len(result)