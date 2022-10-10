# from collections import deque

# def solution(priorities, location):
#     priorities = deque([[idx, priority] for idx, priority in enumerate(priorities)])
#     stack = []
#     while priorities:
#         target = priorities.popleft()
#         if any(target[1] < priority[1] for priority in priorities):
#             priorities.append(target)
#         else:
#             stack.append(target)
#     for i in range(len(stack)):
#         if location == stack[i][0]:
#             return i+1
      
from collections import deque
        
def solution(priorities, location):
    priorities = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    answer = 0
    while True:
        current_priority = priorities.popleft()
        if any(current_priority[1] < priority[1] for priority in priorities):
            priorities.append(current_priority)
            # print(current_priority)
            # print(priorities)
        else:
            answer += 1
            # print(current_priority)
            # print(priorities)
            # print(answer)
            if current_priority[0] == location :
                return answer