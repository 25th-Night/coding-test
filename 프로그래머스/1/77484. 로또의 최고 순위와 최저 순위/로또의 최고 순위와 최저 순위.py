from collections import defaultdict

def solution(lottos, win_nums):
    correct = defaultdict(int)
    for num in win_nums:
        correct[num] = 1
    for num in lottos:
        if num and num in correct:
            correct[num] -= 1
    cnt = 0
    for num in correct:
        if not correct[num]:
            cnt += 1
    return [7 - max(cnt+lottos.count(0), 1), 7 - max(cnt, 1)]