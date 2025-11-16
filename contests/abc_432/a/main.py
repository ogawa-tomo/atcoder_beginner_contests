A = list(map(int, input().split()))
A.sort(reverse=True)
num = ""
for a in A:
    num += str(a)
print(int(num))
