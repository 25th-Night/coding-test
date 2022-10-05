# import math

# def solution(clothes):
#     answer = {}
#     for p in clothes:
#         answer[p[1]] = answer.get(p[1], 0) + 1
#     array = answer.values()
#     array = [i+1 for i in array]
#     return math.prod(array) -1


from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer