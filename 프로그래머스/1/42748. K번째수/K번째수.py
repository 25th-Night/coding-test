def solution(array, commands):
    return [sorted(array[s-1:e])[i-1] for s,e,i in commands]