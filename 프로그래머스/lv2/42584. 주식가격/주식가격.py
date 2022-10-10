# from collections import deque

# def solution(prices):
#     length = len(prices)
#     answer = [0] * length
    
#     for i in range(length):
#         for j in range(i+1, length):
#             answer[i] +=1
#             if prices[i] > prices[j]:
#                 break
#     return answer


def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        # print(f"i : {i}")
        while stack and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            # print(f"past : {past}")
            # print(f"_ : {_}")
            answer[past] = i - past
            # print(f"answer : {answer}")
        stack.append([i, prices[i]])
        # print(f"stack : {stack}")
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
        # print(f"answer : {answer}")
    return answer

prices = [1,2,3,2,3]
solution(prices)