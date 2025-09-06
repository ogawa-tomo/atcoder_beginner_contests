T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    sorted_s = S[1 : N - 1].sort()
    # domino = [S[0], *((S[1 : N - 1]).sort()), S[N - 1]]
    domino = [S[0], *sorted(S[1 : N - 1]), S[N - 1]]
    # print(domino)
    current_i = 0
    target_i = 1
    current = domino[current_i]
    answer = 2
    while target_i < N:
        if domino[N - 1] <= current * 2:
            break
        elif domino[target_i] <= current * 2:
            target_i += 1
        elif current_i + 1 < target_i and domino[target_i - 1] <= current * 2:
            current_i = target_i - 1
            target_i = current_i + 1
            current = domino[current_i]
            answer += 1
        else:
            answer = -1
            break
    print(answer)
