from collections import deque

def solution(prices):
    length = len(prices)
    answer = [0] * length
    
    for i in range(length):
        for j in range(i+1, length):
            answer[i] +=1
            if prices[i] > prices[j]:
                break
    return answer