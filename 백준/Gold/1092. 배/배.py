import sys

n = int(input())
cranes = sorted(map(int, input().split()), reverse=True)

m = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()


positions = [0] * n

checked = [False] * m

result = 0
count = 0

while True:
    if count == len(boxes):
        break
    for i in range(n):
        while positions[i] < len(boxes):
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)