from collections import deque

def solution(s):
    q = deque(s)
    s = []
    while q:
        if (not s or (s and s[-1] == "(")) and q[0] == "(":
            s.append(q.popleft())
        elif s and s[-1] == "(" and q[0] == ")":
            s.pop()
            q.popleft()
        else:
            return False
    return True if not s else False