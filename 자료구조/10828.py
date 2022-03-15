import sys

input = sys.stdin.readline

n = int(input())

s = []

for i in range(n):
    query = input().split()
    if query[0] == 'push':
        s.append(query[1])
    elif query[0] == 'pop':
        if len(s):
            print(s.pop())
        else:
            print(-1)
    elif query[0] == 'size':
        print(len(s))
    elif query[0] == 'empty':
        if len(s):
            print(0)
        else:
            print(1)
    elif query[0] == 'top':
        if len(s):
            print(s[-1])
        else:
            print(-1)