import sys

n = int(input())
k = int(input())

if k >= n:
    print(0)
    sys.exit()
    
arr = sorted(map(int, input().split()))

dist = []
for i in range(1, n):
    dist.append(arr[i] - arr[i-1])
dist.sort(reverse=True)

for i in range(k-1):
    dist[i] = 0

print(sum(dist))