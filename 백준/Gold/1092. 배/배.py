import sys
input = sys.stdin.readline

N = int(input())
cranes = sorted(map(int, input().split()), reverse=True)
M = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

cnt = 0

if cranes[0] < boxes[0]:
    cnt = -1
else:
    while boxes:
        for c in cranes:
            if boxes and c < boxes[-1]:
                continue
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break
        cnt += 1

print(cnt)