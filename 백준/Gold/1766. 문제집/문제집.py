from collections import defaultdict
from heapq import heappop, heappush

graph = defaultdict(list)
indegree = defaultdict(int)

N, M = map(int, input().split())

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1

heap = []

for i in range(1, N+1):
    if not indegree[i]:
        heappush(heap, i)

result = []

while heap:
    cn = heappop(heap)
    result.append(cn)
    for nn in graph[cn]:
        indegree[nn] -= 1
        if not indegree[nn]:
            heappush(heap, nn)
            
print(" ".join(map(str, result)))