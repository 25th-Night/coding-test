# from collections import deque

# def solution(s):
#     s = deque(s)
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
#     return True if not arr else False


def solution(s):
    x = 0
    for w in s:
        if x < 0:
            break
        else:
            if w == "(":
                x += 1 
            elif w == ")":
                x -= 1
    return x==0