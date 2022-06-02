import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))

answer = [0]*(n+m)

i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i<n or j<m:
    # 리스트 B의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
    if j>=m or (i<n and a[i]<=b[j]):
        answer[k] = a[i]
        i+=1
    # 리스트 A의 모든 원소가 처리되었거나, 리스트 B의 원소가 더 작을 때
    else:
        answer[k] = b[j]
        j+=1
    k+=1

for i in answer:
    print(i,end=' ')