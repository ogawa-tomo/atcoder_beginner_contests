Q = int(input())

sound = 0
playing = False
for _ in range(Q):
    a = int(input())
    if a == 1:
        sound += 1
    elif a == 2:
        if sound >= 1:
            sound -= 1
    elif a == 3:
        playing = not playing

    if playing and sound >= 3:
        print("Yes")
    else:
        print("No")
