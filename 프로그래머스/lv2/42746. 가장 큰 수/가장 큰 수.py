# def solution(numbers):
#     # 오답
#     return ''.join(sorted(list(map(str, numbers)), reverse=True))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))
    