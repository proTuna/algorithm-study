import sys

input = sys.stdin.readline

n = int(input())
postfix = list(input().rstrip())
v = []
s = []

for _ in range(n):
    v.append(input().rstrip())

for i in range(len(postfix)):
    if postfix[i].isalpha():
        postfix[i] = v[ord(postfix[i])-ord('A')]

for i in postfix:
    if i.isdigit():
        s.append(int(i))
    else:
        if i =='+':
            a = s.pop()
            b = s.pop()
            s.append(b+a)
        elif i =='-':
            a = s.pop()
            b = s.pop()
            s.append(b-a)
        elif i =='*':
            a = s.pop()
            b = s.pop()
            s.append(b*a)
        elif i =='/':
            a = s.pop()
            b = s.pop()
            s.append(b/a)

print(f'{s[0]:.2f}')