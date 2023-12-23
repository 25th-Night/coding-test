def solution(brown, yellow):
    total = brown + yellow
    for n in range(total//3, int(total**0.5)-1, -1):
        if not total % n and 2 * (n + total//n) - 4 == brown:
            return [n, total//n]