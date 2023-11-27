from collections import deque

def solution(priorities, location):
    priorities = [(idx, priority) for idx, priority in enumerate(priorities)]
    
    priorities = deque(priorities)
    
    executed = []
    while priorities:
        target_priority = priorities.popleft()
        if any(target_priority[1] < priority[1] for priority in priorities):
            priorities.append(target_priority)
        else:
            executed.append(target_priority)
    
    for idx, process in enumerate(executed):
        if location == process[0]:
            return idx + 1