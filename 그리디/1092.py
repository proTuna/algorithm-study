import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 크레인의 수
c_w = list(map(int, input().rstrip().split())) # 각 크레인의 무게 제한
m = int(input().rstrip()) # 박스의 수
b_w = list(map(int, input().rstrip().split())) # 각 박스의 무게

c_w.sort(reverse=True)
b_w.sort(reverse=True)
answer = 0

if c_w[0] < b_w[0]:
    print(-1)
else:
    while len(b_w)>0:
        answer+=1
        for i in range(n):
            for j in range(len(b_w)):
                if c_w[i] >= b_w[j]:
                    b_w.pop(j)
                    break
    print(answer)