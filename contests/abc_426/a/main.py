X, Y = map(str, input().split())
# print(X, Y)

if X == "Lynx":
    print("Yes")
elif X == "Serval":
    if Y == "Serval" or Y == "Ocelot":
        print("Yes")
    else:
        print("No")
elif X == "Ocelot":
    if Y == "Ocelot":
        print("Yes")
    else:
        print("No")
