from collections import deque

def solution(number, k):
    result_number_length = len(number) - k
    result = deque()
    number_list = deque(number)
    
    while number_list and k:
        result.append(number_list.popleft())
        while result and number_list and result[-1] < number_list[0] and k:
            result.pop()
            k -= 1
    
    if k:
        result = list(result)[:-k]
    
    return "".join(result) + "".join(number_list)
    