from heapq import heapify, heappop, heappush, nlargest, nsmallest
from collections import deque

def solution(operations):
    ops = deque(operations)
    answer = []
    while ops:
        cmd, num = ops.popleft().split(" ")
        if cmd == "I":
            heappush(answer, int(num))
        elif answer and cmd == "D":
            if num == "-1":
                heappop(answer)
            else:
                answer = nlargest(len(answer), answer)[1:]
                heapify(answer)
    return nlargest(1, answer) + nsmallest(1, answer) if answer else [0, 0]