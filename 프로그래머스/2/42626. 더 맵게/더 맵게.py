from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        f = heappop(scoville)
        s = heappop(scoville)
        heappush(scoville, f+s*2)
        cnt += 1
    return cnt