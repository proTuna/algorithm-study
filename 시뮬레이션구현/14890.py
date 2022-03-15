import sys
input = sys.stdin.readline

def go(a,l):
    n = len(a)
    c  = [False]*n
    for i in range(1,n):
        if a[i-1] != a[i]:
            dif = abs(a[i-1]- a[i])
            if dif != 1:
                return False
            if a[i-1]< a[i]:
                for j in range(1,l+1):
                    if i-j <0: # 경사로를 놓다가 범위를 벗어나는 경우
                        return False
                    if a[i-1] != a[i-j]: # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개 연속되지 않은 경우
                        return False
                    if c[i-j]: # 경사로를 놓은 곳에 또 경사로를 놓은 경우
                        return False
                    c[i-j] = True
            else:
                for j in range(l):
                    if i+j >= n :
                        return False
                    if a[i] != a[i+j]:
                        return False
                    if c[i+j]:
                        return False
                    c[i+j] = True
    return True

n,l = map(int,input().rstrip().split())
a = [list(map(int,input().rstrip().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    d = a[i]
    if go(d,l):
        cnt+=1
for j in range(n):
    d = [a[i][j] for i in range(n)]
    if go(d,l):
        cnt+=1
print(cnt)

