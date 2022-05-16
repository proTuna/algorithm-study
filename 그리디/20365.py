import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = input().rstrip()

answer1 = 1
color = 'R'
stack = []
for s in l:
    if len(stack) == 0:
        stack.append(s)
        if s == color:
            answer1+=1
    else:
        if s == color and stack[-1] != color:
            answer1+=1
            stack.append(s)
        else:
            stack.append(s)

answer2 = 1
color = 'B'
stack = []
for s in l:
    if len(stack) == 0:
        stack.append(s)
        if s == color:
            answer2+=1
    else:
        if s == color and stack[-1] != color:
            answer2+=1
            stack.append(s)
        else:
            stack.append(s)
print(min(answer1,answer2))