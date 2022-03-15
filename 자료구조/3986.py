import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    s = input().rstrip()
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if len(stack)==0:
        cnt +=1

print(cnt)