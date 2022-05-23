import sys
input = sys.stdin.readline

n = int(input().rstrip())
p = []
answer = 0
totalp = 0

for _ in range(n):
    v_n, v_p = map(int,input().rstrip().split())
    totalp += v_p
    p.append([v_n,v_p])

p.sort(key=lambda x : x[0])

# 인구의 합이 절반에 속하는 부분에 우체국을 설치하는 게 좋다.
cnt = 0
for i in range(n):
    cnt+=p[i][1]
    if cnt >= totalp/2:
        answer = p[i][0]
        break
print(answer)