def solution(citations):
    citations.sort()
    idx = len(citations) // 2
    target = citations[idx]
    while True:
        right = [num for num in citations if num >= target]
        if len(right) >= target:
            return target
        else:
            target -= 1
    return target


# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0