import sys

input = sys.stdin.readline

stick = list(input().rstrip())

s=[]
cnt=0
for i in range(len(stick)):
    if stick[i]=='(':
        s.append(stick[i])
    else:
        s.pop()
        if stick[i-1]=='(':
            cnt+=len(s)
        else:
            cnt+=1
print(cnt)