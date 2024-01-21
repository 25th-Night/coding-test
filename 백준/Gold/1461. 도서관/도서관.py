N, M = map(int, input().split())
books = sorted(map(int, input().split()))
longest = max(max(books), -min(books))

plus, minus = [], []
minus = []
for book in books:
    if book > 0:
        plus.append(book)
    else:
        minus.append(book)
plus.sort(reverse=True)
minus.sort()

total = 0
for p in plus[::M]:
    total += 2*p
for m in minus[::M]:
    total += -2*m

print(total - longest)