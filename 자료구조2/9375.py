import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    a = {}
    cnt = 1
    for _ in range(N):
        name, c_type = map(str,input().rstrip().split())
        a[c_type] = a.get(c_type, 0) + 1
    for v in a.values():
        cnt*=v+1
    print(cnt-1)
