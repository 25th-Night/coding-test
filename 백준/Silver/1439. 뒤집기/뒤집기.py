arr = list(input())

cnt0 = 0
cnt1 = 0

while arr:
    if arr[-1] == "0":
        cnt0 += 1
        arr.pop()
        while arr and arr[-1] =="0":
            arr.pop()
    elif arr[-1] == "1":
        cnt1 += 1
        arr.pop()
        while arr and arr[-1] == "1":
            arr.pop()

print(min(cnt0, cnt1))