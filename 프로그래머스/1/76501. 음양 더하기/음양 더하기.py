from functools import reduce


def mul(x, y):
    return x if y else -x

def solution(absolutes, signs):
    return reduce(lambda x, y: x+y, [mul(num, s) for num, s in zip(absolutes, signs)], 0)