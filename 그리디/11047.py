import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
l = [int(input().rstrip()) for _ in range(n)]
answer = 0

#1
for i in range(n-1,-1,-1):
    if k%l[i] == k:
        continue
    if k == 0:
        break
    answer += k//l[i]
    k = k%l[i]

print(answer)


#2
l.sort(reverse=True)

for i in l:
    answer += k//i
    k%=i
print(answer)