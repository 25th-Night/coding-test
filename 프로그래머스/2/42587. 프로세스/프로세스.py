from collections import deque

def solution(priorities, location):
    
    priorities = deque(priorities)
    
    order = 0
    while True:
        now = priorities.popleft()
        if any(now < priority for priority in priorities):
            priorities.append(now)
            location = location - 1 if location else len(priorities) - 1
        else:
            order += 1
            if not location:
                return order
            location -= 1