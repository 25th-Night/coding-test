def solution(array, commands):
    return  [sorted(array[start-1:end])[index-1] for start,end,index in commands]
