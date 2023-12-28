def solution(s, skip, index):
    li = list(range(97, 123))
    for c in skip:
        li.remove(ord(c))
    result = ""
    for c in s:
        result += chr(li[(li.index(ord(c)) + index) % len(li)])
    return result