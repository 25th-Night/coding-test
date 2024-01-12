from heapq import heappop, heappush

import sys

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    n = int(input())
    if not n:
        print(heappop(heap)[1] if heap else 0)
    else:
        heappush(heap, (abs(n), n))