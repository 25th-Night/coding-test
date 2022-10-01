def solution(nums):
    l1 = len(nums)
    num2 = set(nums)
    l2 = len(num2)
    return l2 if l1//2 >= l2 else l1//2