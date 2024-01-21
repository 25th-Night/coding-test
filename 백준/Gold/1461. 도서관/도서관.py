from heapq import heappop, heappush

N, M = map(int, input().split())
bs = list(map(int, input().split()))
longest = max(max(bs), -min(bs))
p, n = [], []

for b in bs:
    if b > 0:
        heappush(p, -b)
    else:
        heappush(n, b)
        
result = 0

while p:
    result += heappop(p)
    for _ in range(M-1):
        if p:
            heappop(p)
while n:
    result += heappop(n)
    for _ in range(M-1):
        if n:
            heappop(n)
            
print(-2*result - longest)