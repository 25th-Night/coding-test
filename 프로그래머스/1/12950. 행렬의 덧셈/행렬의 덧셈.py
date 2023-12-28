def solution(arr1, arr2):
    return [[x+y for x, y in zip(sa1, sa2)] for sa1, sa2 in zip(arr1, arr2)]