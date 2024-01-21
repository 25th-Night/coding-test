n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())

left, right = 0, len(arr)-1

cnt = 0
while left < right:
    if arr[left] + arr[right] > x:
        right -= 1
    elif arr[left] + arr[right] == x:
        cnt += 1
        left += 1
        right -= 1
    else:
        left += 1
print(cnt)