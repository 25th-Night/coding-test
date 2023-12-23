from collections import deque

def solution(number, k):
    nums = deque(number)
    stack = []
    
    while nums and k:
        while nums and stack and stack[-1] < nums[0] and k:
            stack.pop()
            k -= 1
        stack.append(nums.popleft())
    if k:
        stack = stack[:-k]
    
    return "".join(stack + list(nums))