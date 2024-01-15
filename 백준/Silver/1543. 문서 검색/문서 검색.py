s = input()
t = input()

result = 0
while True:
    if s.startswith(t):
        result += 1
        s = s[len(t):]
    else:
        s = s[1:]
    if not s:
        break
print(result)