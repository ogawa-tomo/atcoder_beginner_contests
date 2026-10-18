S1 = input()
S2 = input()

if S1[0] == "A":
    if S1[1] == "D":
        print("Yes")
    elif S2[0] == "D":
        print("Yes")
    else:
        print("No")
elif S1[1] == "A":
    if S1[0] == "D" or S2[1] == "D":
        print("Yes")
    else:
        print("No")
elif S2[0] == "A":
    if S2[1] == "D" or S1[0] == "D":
        print("Yes")
    else:
        print("No")
elif S2[1] == "A":
    if S2[0] == "D" or S1[1] == "D":
        print("Yes")
    else:
        print("No")
