from heapq import heappop, heappush, nlargest, heapify
from collections import deque

def extract_number(operation):
    return int(operation.split(" ")[-1])

def solution(operations):
    queue = []
    operations = deque(operations)
    
    while operations:
        operation = operations.popleft()
        if operation.startswith("I"):
            if not queue:
                queue.append(extract_number(operation))
            else:
                heappush(queue, extract_number(operation))
        elif operation.startswith("D"):
            if operation[-2] == "-":
                if len(queue) > 1:
                    heappop(queue)
                else:
                    queue = []
            else:
                queue = queue[:-1]
        
    if not queue:
        queue = [0, 0]
    
    queue.sort()
    return [queue[-1], queue[0]]
    