import sys
input = sys.stdin.readline

n = int(input().rstrip())

ropes = []

for i in range(n):
    rope = int(input().rstrip())
    ropes.append(rope)

ropes.sort(reverse=True)

result = 0
for i in range(n):
    max_w = ropes[i] * (i+1)
    if max_w > result:
        result = max_w

print(result)