import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0 # 현재 부분수열의 홀수의 갯수
start, end = 0, 0 # 시작, 끝 포인터
size, size_max = 0, 0 # 현재 부분수열의 길이, 가장 긴 짝수 부분수열의 길이
flag = 1 # end가 마지막이면 끝내게 하기 위한 값

for start in range(n):
    while cnt <= k and flag:
        if l[end] % 2: # 현재 수가 홀수이면
            if cnt == k: # 홀수의 개수가 k이면 while문 종료
                break
            cnt += 1 # 홀수의 개수 +1
        size += 1
        if end == n - 1: # 마지막 원소에 도착하면 끝낸다.
            flag = 0
            break
        end += 1
    
    # 가장 긴 짝수 부분수열의 길이 업데이트
    if size_max < size - cnt:
        size_max = size - cnt
    
    # 시작 포인터를 한칸씩 이동시킨다.
    if l[start] % 2:
        cnt -= 1
        
    size -= 1

print(size_max)