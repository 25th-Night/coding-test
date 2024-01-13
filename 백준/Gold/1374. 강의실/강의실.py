from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())

lecture = []
for _ in range(N):
    n, s, e = map(int, input().split())
    heappush(lecture, (s, e))

end = heappop(lecture)[1]
heap = [end]
cnt = 1

for i in range(N-1):
    cs, ce = heappop(lecture)
    end = heappop(heap)
    if cs < end:
        heappush(heap, end)
        cnt += 1
    heappush(heap, ce)

print(cnt)
