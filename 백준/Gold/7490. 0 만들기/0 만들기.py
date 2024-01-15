from copy import deepcopy

def recursive(ops, arr, n):
    if len(arr) == n:
        ops.append(deepcopy(arr))
        return
    
    arr.append(" ")
    recursive(ops, arr, n)
    arr.pop()
    
    arr.append("+")
    recursive(ops, arr, n)
    arr.pop()
    
    arr.append("-")
    recursive(ops, arr, n)
    arr.pop()
    
T = int(input())

for _ in range(T):
    ops = []
    n = int(input())
    recursive(ops, [], n-1)
    nums = list(map(str, range(1, n+1)))
    
    for op in ops:
        s = ""
        for i in range(n-1):
            s += nums[i] + op[i]
        s += nums[-1]
        
        if eval(s.replace(" ", "")) == 0:
            print(s)
    print()