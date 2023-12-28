from heapq import heappop, heappush, nsmallest

def solution(k, score):
    answer = []
    honor = []
    for i, s in enumerate(score):
        if i < k:
            heappush(honor, s)
        else:
            curr = nsmallest(1, honor)[0]
            if curr < s:
                heappop(honor)
                heappush(honor, s)
        answer.append(nsmallest(1, honor)[0])
    return answer