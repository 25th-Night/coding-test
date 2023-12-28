def solution(x, n):
    if not x:
        return [0] * n
    return list(range(min(x, x*n), max(x,x*n)+1, abs(x))) if x > 0 else sorted(range(min(x, x*n), max(x,x*n)+1, abs(x)), reverse=True)