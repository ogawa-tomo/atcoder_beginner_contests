N = int(input())
X = list(map(int, input().split()))

for x in X:
    if x >= 0:
        print("No")
        exit()
print("Yes")
