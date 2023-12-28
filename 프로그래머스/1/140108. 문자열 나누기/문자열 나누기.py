from collections import deque

def solution(s):
    s = deque(s)
    dic = {"c":0, "a":0}
    cnt = 0
    while s:
        c = s.popleft()
        dic["c"] += 1
        while s and dic["c"] != dic["a"]:
            n = s.popleft()
            if n == c:
                dic["c"] += 1
            else:
                dic["a"] += 1
        cnt += 1
        dic = {"c":0, "a":0}
        
    return cnt