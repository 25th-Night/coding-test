# def solution(participant, completion):

#     participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p


# def solution(participant, completion):
#     dic = {i:0 for i in participant}
#     for i in participant:
#         dic[i] += 1
#     for j in completion:
#         dic[j] -= 1
#     for k in participant:
#         if dic[k] != 0:
#             return k
       
    
# def solution(participant, completion):
#     dic = {}
#     for i in participant:
#         dic[i] = dic.get(i, 0) + 1
#     for j in completion:
#         dic[j] -= 1
#     for k in participant:
#         if dic[k] != 0:
#             return k