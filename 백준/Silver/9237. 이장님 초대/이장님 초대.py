N = int(input())
trees = sorted(map(int, input().split()), reverse=True)

result = 0

for i, t in enumerate(trees, 2):
    result = max(result, i+t)

print(result)