def solution(sequence, k):
    n = len(sequence)
    data = sequence

    result = []
    total = 0
    end = 0

    for start in range(n):
        while total < k and end < n:
            total += data[end]
            end += 1
        if total == k:
            result.append([start, end - 1])
        total -= data[start]
    
    result.sort(key = lambda x : (x[1] - x[0], [0]))
      
    return result[0]