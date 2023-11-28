from collections import deque

def sum_of_equatorial_sequences(digit):
    return (5**digit - 1) // 4

def solution(word):
    character_list = ["A", "E", "I", "O", "U"]
    result = 0
    word = deque(word)
    checked_list_cnt = 0
    while word:
        char = word.popleft()
        period = sum_of_equatorial_sequences(5 - checked_list_cnt)
        if char.startswith("A"):
            result += period * 0 + 1
        if char.startswith("E"):
            result += period * 1 + 1
        if char.startswith("I"):
            result += period * 2 + 1
        if char.startswith("O"):
            result += period * 3 + 1
        if char.startswith("U"):
            result += period * 4 + 1
        checked_list_cnt += 1
    return result