from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    trucks = deque(truck_weights)
    time = 0
    while trucks:
        bridge_weight -= bridge.popleft()
        if bridge_weight + trucks[0] <= weight:
            bridge_weight += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
        time += 1
    time += bridge_length
    
    return time