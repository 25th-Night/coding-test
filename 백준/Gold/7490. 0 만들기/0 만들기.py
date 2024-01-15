from itertools import product

T = int(input())

for _ in range(T):
    n = int(input())
    ops_list = list(product((" ", "+", "-"), repeat=n-1))
    nums = list(map(str, range(1, n+1)))
    
    for ops in ops_list:
        s = ""
        for n, o in zip(nums[:-1], ops):
            s += n+o
        s += nums[-1]
        
        if eval(s.replace(" ", "")) == 0:
            print(s)
    print()