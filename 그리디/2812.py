import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
nums = list(map(int,input().rstrip()))
answer = []

cnt = k
for i in range(n):
    while cnt>0 and answer:
        if answer[-1] < nums[i]:
            answer.pop()
            cnt-=1
        else:
            break
    answer.append(nums[i])

print(''.join(map(str,answer[:n-k])))