def solution(routes):
    routes.sort(key=lambda x:x[1])
    cnt = 0
    cam = -30001
    for s, e in routes:
        if cam < s:
            cnt += 1
            cam = e
    return cnt