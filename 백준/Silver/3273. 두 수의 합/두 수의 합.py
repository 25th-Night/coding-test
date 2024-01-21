n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())

left, right = 0, len(arr)-1
cnt = 0

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == x:
        cnt += 1
        left += 1
        right -= 1
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print(cnt)
