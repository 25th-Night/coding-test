def solution(n):
    result = ""
    while n:
        n, r = divmod(n, 3)
        result += str(r)
    num = 0
    for i, n in enumerate(result):
        num += 3**(len(result)-1-i) * int(n)
    return num