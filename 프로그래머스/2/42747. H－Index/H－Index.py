def check_idx(citations, idx):
    upper_quotation_length = len(list(filter(lambda x: x>=idx, citations)))
    return upper_quotation_length >= idx

def solution(citations):
    for i in range(max(citations)):
        if not check_idx(citations, i):
            return i-1
    return 0