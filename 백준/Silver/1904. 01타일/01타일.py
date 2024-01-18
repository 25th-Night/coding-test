N = int(input())

a, b = 1, 2
n = 1

while n < N:
    a, b = b, (a+b) % 15746
    n += 1

print(a)