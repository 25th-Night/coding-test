import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if not x:
        print(0 if not heap else heappop(heap))
    else:
        heappush(heap, x)