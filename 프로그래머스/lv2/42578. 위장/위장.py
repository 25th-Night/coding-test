import math

def solution(clothes):
    answer = {}
    for p in clothes:
        answer[p[1]] = answer.get(p[1], 0) + 1
    array = answer.values()
    array = [i+1 for i in array]
    return math.prod(array) -1