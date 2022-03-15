import sys

input = sys.stdin.readline

def sol():
    s = input().rstrip()
    stack = []
    ans = ''

    for i in s:
        if i.isalpha():
            ans+=i
        else:
            if i == '(':
                stack.append(i)
            elif i == '*' or i == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    ans+=stack.pop()
                stack.append(i)
            elif i == '+' or i == '-':
                while stack and stack[-1] != '(':
                    ans+= stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()
    while stack:
        ans+=stack.pop()
    print(ans)
    

if __name__ == '__main__':
    sol()