from collections import deque

N, K = map(int, input().split())
num = input()

checked = deque()
num = deque(num)

while num and K:
    checked.append(num.popleft())
    while checked and num and checked[-1] < num[0] and K:
        checked.pop()
        K -= 1

if K:
    checked = list(checked)[:-K]

print(int("".join(checked) + "".join(num)))
