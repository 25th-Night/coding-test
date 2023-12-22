def solution(numbers, target):
    dp = [[0]]
    for n in numbers:
        tmp = []
        for x in dp[-1]:
            tmp += [x-n, x+n]
        dp.append(tmp)
    return dp[-1].count(target)