import sys

input = sys.stdin.readline


s = list(input().rstrip())


# 올바른 괄호열인지 검사하는 함수
def is_valid(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        else:
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    if not stack:
        return True
    return False


def sol(s):
    stack = []
    for i in range(len(s)):
        print(stack)
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        else:
            if s[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:
                    tmp = 0
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j] == '(':
                            stack[-1] = tmp*2
                            break
                        else:
                            tmp += stack[-1]
                            stack.pop()
            else:
                if stack[-1] == '[':
                    stack[-1] = 3
                else:
                    tmp = 0
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j] == '[':
                            stack[-1] = tmp*3
                            break
                        else:
                            tmp += stack[-1]
                            stack.pop()
    return sum(stack)

if is_valid(s):
    print(sol(s))
else:
    print(0)

