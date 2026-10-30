N = int(input())
L = list(map(int, input().split()))

left = 0
right = sum(L)
answer = right
for l in L:
    left += l
    right -= l
    answer = min(answer, abs(left - right))

print(answer)
