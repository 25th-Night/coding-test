def solution(s, n):
    answer = ""
    for c in s:
        if c.isalpha():
            if c.lower() == c:
                answer += chr(ord(c) + n) if ord(c) + n <= 122 else chr(ord(c) + n - 26)
            else:
                answer += chr(ord(c) + n) if ord(c) + n <= 90 else chr(ord(c) + n - 26)
        else:
            answer += " "
    return answer