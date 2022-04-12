# 비트 마스크로 문제 해결
import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int,input().rstrip().split()))
c = [False]*(n*100000+10)

for i in range(1<<n):
    s = 0
    for j in range(n):
        if (i&(1<<j)):
            s+=a[j]
    c[s] = True

i = 1
while True:
    if c[i] == False:
        break
    i+=1
print(i)