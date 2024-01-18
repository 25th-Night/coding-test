import sys
from heapq import heappop, heappush

N = int(input())

heap = []

for _ in range(N):
    heappush(heap, int(input()))

result = 0
while heap:
    x = heappop(heap)
    if heap:
        y = heappop(heap)
        result += x + y
        heappush(heap, x + y)

print(result)