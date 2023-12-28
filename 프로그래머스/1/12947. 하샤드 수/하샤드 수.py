def solution(x):
    return not x % sum(map(int,list(str(x))))