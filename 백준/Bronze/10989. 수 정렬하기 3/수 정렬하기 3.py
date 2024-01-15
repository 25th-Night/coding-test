import sys

input = sys.stdin.readline

N  = int(input())
dp = [0] * 10001

for _ in range(N):
    i = int(input())
    dp[i] += 1

for i in range(10001):
    for _ in range(dp[i]):
        print(i)