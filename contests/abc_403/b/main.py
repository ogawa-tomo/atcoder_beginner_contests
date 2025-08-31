T = list(input())
U = list(input())

for i in range(len(T) - len(U) + 1):
    success = True
    for j in range(len(U)):
        t = T[i + j]
        s = U[j]
        if t != "?" and t != s:
            success = False
            break
    if success:
        print("Yes")
        exit()
print("No")
