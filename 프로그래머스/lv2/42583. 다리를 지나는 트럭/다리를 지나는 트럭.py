# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     truck_weights = deque(truck_weights)
#     bridge = deque([0] * bridge_length)
#     sec = 0
#     while bridge:
#         sec += 1
#         bridge.popleft()
#         if truck_weights:
#             if sum(bridge)+truck_weights[0] <= weight:
#                 bridge.append(truck_weights.popleft())
#             else:
#                 bridge.append(0)
#     return sec

def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    sec = 0
    sum_ = sum(q)
    while q:
        sec += 1
        sum_ -= q.pop(0)
        if truck_weights:
            if sum_ + truck_weights[0] <= weight:
                sum_ += truck_weights[0]
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec