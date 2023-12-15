def solution(N, number):
    dp = []
    i = 1
    while True:
        created = {int(str(N) * i)}
        for j in range(i-1):
            for n1 in dp[j]:
                for n2 in dp[-j-1]:
                    created.add(n1 + n2)
                    created.add(n1 - n2)
                    created.add(n1 * n2)
                    if n2:
                        created.add(n1 / n2)
        if number in created:
            return i
        dp.append(created)
        i += 1
        if i >= 9:
            return -1
