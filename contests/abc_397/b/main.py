S = list(input())

answer = 0
odd = True
for s in S:
    if odd:
        if s == "i":
            odd = False
            continue
        else:
            answer += 1
            continue
    else:
        if s == "o":
            odd = True
            continue
        else:
            answer += 1
            continue

if (len(S) + answer) % 2 == 1:
    answer += 1
print(answer)
