from collections import deque

# def solution(s):
#     # 주어진 문자열
#     s = deque(s)
#     # stack으로 활용할 문자열
#     arr = deque([])
#     while s:
#         if s[0] == "(":
#             s.popleft()
#             arr.append("(")
#         else:
#             if not arr:
#                 return False
#             elif arr[-1] == "(":
#                 arr.pop()
#                 s.popleft()
#     return not arr

def solution(s):
    answer = []
    for i in s:
        if i == "(":
            answer.append(i)
        else:
            if not answer:
                return False
            elif answer[-1] == "(":
                answer.pop()
    return not answer





# def solution(s):
#     score = 0
#     for w in s:
#         if score < 0:
#             return 0
#         else:
#             if w == "(":
#                 score += 1 
#             elif w == ")":
#                 score -= 1
#     return score == 0