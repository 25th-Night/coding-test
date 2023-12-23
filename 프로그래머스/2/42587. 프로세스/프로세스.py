from collections import deque

def solution(priorities, location):
    ps = deque(priorities)
    order = 1
    while True:
        c = ps.popleft()
        if any(c < p for p in ps):
            ps.append(c)
            location = location -1 if location else len(ps) - 1
        else:
            if not location:
                return order
            order += 1
            location -= 1