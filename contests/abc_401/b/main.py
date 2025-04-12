N = int(input())
answer = 0
state = "logout"
for _ in range(N):
    s = input()
    if s == "login":
        state = "login"
    elif s == "logout":
        state = "logout"
    elif s == "public":
        pass
    elif s == "private":
        if state == "logout":
            answer += 1

print(answer)
