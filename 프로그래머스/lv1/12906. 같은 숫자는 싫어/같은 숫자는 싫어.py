def solution(arr):
    answer = [arr[0]]
    length = len(arr)
    for i in range(1,length):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer
            








# def solution(arr):
#     return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i+1:i+2]]