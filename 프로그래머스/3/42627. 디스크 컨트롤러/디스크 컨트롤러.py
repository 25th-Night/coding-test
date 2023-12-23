from heapq import heappop, heappush

def solution(jobs):
    s, e = -1, 0
    f, t = 0, 0
    heap = []
    while f < len(jobs):
        for job in jobs:
            if s < job[0] <= e:
                heappush(heap, (job[1], job[0]))
        if heap:
            cn, cs = heappop(heap)
            s = e
            e += cn
            t += e - cs
            f += 1
        else:
            e += 1
    return t // f