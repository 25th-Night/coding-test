def solution(a, b, n):
    drink = 0
    rest = n
    cnt = 1
    while True:
        q, r = divmod(rest, a)
        new = q * b
        drink += new
        rest = new + r
        if rest < a:
            break
    return drink