from collections import defaultdict

def solution(keymap, targets):
    dic = defaultdict(int)
    for key in keymap:
        for i, c in enumerate(key, 1):
            if c not in dic:
                dic[c] = i
            else:
                dic[c] = min(dic[c], i)
                
    result = []
    for t in targets:
        total = 0
        stop = False
        for c in t:
            if c not in dic:
                stop = True
                result.append(-1)
                break
            total += dic[c]
        if stop:
            continue
        result.append(total)
    return result