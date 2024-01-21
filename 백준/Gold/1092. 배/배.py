N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
cranes.sort(reverse=True)
boxes.sort(reverse=True)

t = 0
if cranes[0] < boxes[0]:
    t = -1
else:
    while boxes:
        for c in cranes:
            if boxes and c < boxes[-1]:
                break
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break
        t += 1

print(t)

