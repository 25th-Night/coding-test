from collections import deque

def solution(prices):
    prices = deque(prices)
    result = []
    
    while prices:
        price = prices.popleft()
        sec = 0
        for p in prices:
            sec += 1
            if price > p:
                break
        result.append(sec)
        
    return result