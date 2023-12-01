from heapq import heappop, heappush

def solution(jobs): 
    result = 0
    start, now = -1, 0
    idx = 0
    heap = []

    while idx < len(jobs):
        for job_start, job_time in jobs:
            if start < job_start <= now:
                heappush(heap, [job_time, job_start])
        if heap:
            before_job_time, before_job_start = heappop(heap)
            start = now
            now += before_job_time
            result += now - before_job_start
            idx += 1
        else:
            now += 1
    return result // idx