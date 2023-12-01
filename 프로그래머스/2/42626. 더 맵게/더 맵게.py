
from collections import deque

def solution(scoville, K):
    scoville.sort()
    scoville = deque(scoville)
    
    result = 0
    mixed = deque()
    
    while (scoville and scoville[0] < K) or (mixed and mixed[0] < K):
        result += 1
        if len(scoville) + len(mixed) <= 1:
            return -1
        
        food = [0] * 2
        for i in range(2):
            if scoville and mixed:
                if scoville[0] < mixed[0]:
                    food[i] = scoville.popleft()
                else:
                    food[i] = mixed.popleft()
            elif scoville:
                food[i] = scoville.popleft()
            else:
                food[i] = mixed.popleft()
            
        mixed.append(food[0] + food[1] * 2)
        
    return result