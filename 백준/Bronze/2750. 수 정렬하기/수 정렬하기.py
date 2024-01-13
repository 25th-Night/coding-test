import sys

input = sys.stdin.readline

def bubble_sort(data):
    for i in range(len(data)):
        swap = False
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                swap = True
                data[j], data[j+1] = data[j+1], data[j]
        if not swap:
            break
    return data

N = int(input())
data = []

for _ in range(N):
    data.append(int(input()))

data = bubble_sort(data)
for n in data:
    print(n)