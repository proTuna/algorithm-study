import sys
input = sys.stdin.readline

n = int(input().rstrip())
books = []
a = {}

for _ in range(n):
    books.append(input().rstrip())

for book in books:
    a[book] = a.get(book,0) +1

cnt = max(a.values())

answer = []

for v,k in a.items():
    if k == cnt:
        answer.append(v)

print(sorted(answer)[0])