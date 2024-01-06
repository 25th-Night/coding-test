n = int(input())
arr = []
arr.append((0, 0, 0, 0))
for i in range(1, n+1):
    arr.append((i, *map(int, input().split())))

arr.sort(key=lambda x:x[-1])

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + arr[i][2])

max_value = max(dp)
idx = n
result = []

while idx != 0:
    if max_value == dp[idx]:
        result.append(arr[idx][0])
        max_value -= arr[idx][2]
    idx -= 1

result.reverse()
print(len(result))
print("\n".join(map(str, result)))