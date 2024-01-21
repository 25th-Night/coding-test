N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)

total = 0
for x, y in zip(A, B):
    total += x*y

print(total)