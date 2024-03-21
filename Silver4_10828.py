import sys
input=sys.stdin.readline

stack = []
n = int(input())
for _ in range(n):
    argument = input().split()
    arg = argument[0]
    if len(argument)==2:
        num = argument[-1]

    if arg == 'push':
        stack.append(num)
    elif arg == 'pop':
        if len(stack) == 0:
            print(-1)
            continue
        temp = stack.pop()
        print(temp)
    elif arg == 'size':
        print(len(stack))
    elif arg == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif arg == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])