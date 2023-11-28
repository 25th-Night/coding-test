from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    rest = participant - completion
    return list(rest.keys())[0]