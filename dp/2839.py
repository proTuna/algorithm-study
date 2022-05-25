import sys
input = sys.stdin.readline

n = int(input().rstrip())

answer = 0
while True:
    if n%5==0:
        answer+=n//5
        print(answer)
        break
    n-=3
    answer+=1
    if n <0:
        print(-1)
        break