N = int(input())
names: list[str] = []
for _ in range(N):
    s = input()
    names.append(s)
xy = list(input().split())
x = int(xy[0]) - 1
y = xy[1]
# print(names, x, y)
if names[x] == y:
    print("Yes")
else:
    print("No")
