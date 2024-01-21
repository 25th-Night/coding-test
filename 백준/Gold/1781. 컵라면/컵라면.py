from heapq import heappop, heappush

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

heap = []

for d, c in arr:
    heappush(heap, c)
    if d < len(heap):
        heappop(heap)

print(sum(heap))