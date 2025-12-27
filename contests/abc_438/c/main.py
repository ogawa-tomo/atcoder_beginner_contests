N = int(input())
A = list(map(int, input().split()))

stack: list[int] = []
for a in A:
    stack.append(a)
    while True:
        length = len(stack)
        if (
            length >= 4
            and stack[length - 1] == stack[length - 2]
            and stack[length - 1] == stack[length - 3]
            and stack[length - 1] == stack[length - 4]
        ):
            for i in range(4):
                stack.pop()
            continue
        break

# print(stack)
print(len(stack))
