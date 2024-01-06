N = int(input())

if N <= 2:
    print(N)
else:
    a, b = 1, 2
    n = 3
    while n <= N:
        a, b = b % 15746, (a + b) % 15746
        n += 1
    print(b)