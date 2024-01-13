N = int(input())

result = []
for i in range(N):
    age, name = input().split()
    result.append((int(age), i, name))
result.sort()
for p in result:
    print(p[0], p[2])