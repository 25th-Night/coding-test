from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)
    mix_cnt = 0
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        s1 = heappop(scoville)
        s2 = heappop(scoville)
        mixed = s1 + s2 * 2
        mix_cnt += 1
        heappush(scoville, mixed)

    return mix_cnt