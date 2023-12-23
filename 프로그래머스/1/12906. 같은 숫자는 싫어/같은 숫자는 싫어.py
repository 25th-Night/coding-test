def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer or (i and arr[i-1] != arr[i]):
            answer.append(arr[i])
    return answer