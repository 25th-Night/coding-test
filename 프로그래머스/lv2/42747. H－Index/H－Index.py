def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)


# def solution(citations):
#     citations = sorted(citations)
#     print(citations)
#     l = len(citations)
#     print(l)
#     for i in range(l):
#         if citations[i] >= l-i:
#             print(f"i:{i}")
#             print(citations[i])
#             print(l-i)
#             return l-i
#     return 0