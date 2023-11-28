from collections import Counter
from functools import reduce

def mul(data):
    result = reduce(lambda x, y: x * y, data)
    return result

def solution(clothes):
    cloth_sorts = Counter([cloth[1] for cloth in clothes]).values()
    cloth_case = [cloth_sort + 1 for cloth_sort in cloth_sorts]
    
    result = mul(cloth_case) - 1
    return result