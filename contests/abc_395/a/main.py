N = int(input())
A = list(map(int, input().split()))

prev = 0
for i, a in enumerate(A):
    if i == 0:
        prev = a
        continue
    if a <= prev:
        print("No")
        exit()
    prev = a

print("Yes")
