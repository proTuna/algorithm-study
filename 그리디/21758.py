import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int,input().rstrip().split()))

left_prefix_sum = [0]
right_prefix_sum = [0]
sum_value = 0
answer = -int(1e9)

for i in range(n):
    sum_value +=l[i]
    left_prefix_sum.append(sum_value)

sum_value = 0
for i in range(n-1,-1,-1):
    sum_value += l[i]
    right_prefix_sum.append(sum_value)


# 벌통이 양 끝에 있는 경우
for i in range(2,n):
    a = left_prefix_sum[n] - left_prefix_sum[i]
    b = right_prefix_sum[n] - right_prefix_sum[i]
    if i ==2:
        answer = max(a*2, b*2, answer)
    else:
        c = left_prefix_sum[i-1] - left_prefix_sum[1]
        d = right_prefix_sum[i-1] - right_prefix_sum[1]
        answer = max(a*2+c, b*2+d,answer)

# 벌통이 양 끝을 제외한 곳에 있느 경우
for i in range(2,n):
    left = left_prefix_sum[i] - left_prefix_sum[1]
    right = right_prefix_sum[n-i+1] - right_prefix_sum[1]
    answer = max(answer, left+right)

print(answer)