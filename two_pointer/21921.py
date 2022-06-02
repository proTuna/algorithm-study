import sys
input = sys.stdin.readline

n,x = map(int,input().rstrip().split())
p = list(map(int,input().rstrip().split()))

answer = 0
end = 0
cnt = 0
interval_sum = 0
t = 0

for i in range(n):
    while cnt < x and end < n:
        cnt+=1
        interval_sum += p[end]
        end+=1
    if cnt == x:
        if answer == interval_sum:
            t +=1
        if answer < interval_sum:
            answer = interval_sum
            t = 1
    interval_sum -= p[i]
    cnt-=1

if not answer:
    print('SAD')
else:
    print(answer)
    print(t)