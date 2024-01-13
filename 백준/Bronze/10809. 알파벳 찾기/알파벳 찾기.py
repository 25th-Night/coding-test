S = input()

result = [-1] * (ord('z') - ord('a') + 1)

for i, c in enumerate(S):
    if result[ord(c) - ord('a')] == -1:
        result[ord(c) - ord('a')] = i
    
print(*result)