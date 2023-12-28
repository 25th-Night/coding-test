def solution(n):
    if n <= 4:
        return n-1
    else:
        for x in range(2, n):
            if not (n-1) % x:
                return x