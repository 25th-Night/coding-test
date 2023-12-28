from collections import defaultdict

def solution(id_list, report, k):
    report = set(report)
    rs = defaultdict(list)
    cnt = defaultdict(int)
    for r in report:
        x, y = r.split(" ")
        rs[y].append(x)
        cnt[y] += 1
    banned = []
    for user in cnt:
        if cnt[user] >= k:
            banned.append(user)
    result = [0] * len(id_list)
    for banned_user in banned:
        for user in rs[banned_user]:
            result[id_list.index(user)] += 1
    return result