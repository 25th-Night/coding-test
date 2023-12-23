from collections import deque

def solution(progresses, speeds):
    ds = deque([-((p-100)//s) for p, s in zip(progresses, speeds)])
    answer = []
    while ds:
        current = ds.popleft()
        cnt = 1
        while ds and current >= ds[0]:
            ds.popleft()
            cnt += 1
        answer.append(cnt)
    return answer