from collections import deque

def solution(s):
    s = deque(s)
    arr = deque([])
    while s:
        if s[0] == "(":
            s.popleft()
            arr.append("(")
        else:
            if not arr:
                return False
            elif arr[-1] == "(":
                arr.pop()
                s.popleft()
    return True if not arr else False