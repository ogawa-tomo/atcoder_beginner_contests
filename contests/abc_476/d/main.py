# かきかけ
N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

desserts = A
drinks = B
desserts.sort(reverse=True)
drinks.sort()

one_doller_num = X
k_doller_num = Y

answer = 0

# まず、1ドルでデザートを買えるだけ買う
while desserts:
    dessert = desserts[-1]
    if dessert <= one_doller_num:
        one_doller_num -= dessert
        desserts.pop()
        answer += 1
    else:
        desserts[-1] -= one_doller_num
        one_doller_num = 0
        break

print(desserts)


def get_needed_k_bills(price: int):
    answer = price // K
    if price % K != 0:
        answer += 1
    return answer


# まず、おつりが出るドリンクについてだけ考える
i = 0
while i < M:
    drink = drinks[i]

    current_drinks = [drink]
    bills = drink

    # 同じ枚数で買えるドリンクを集める
    needed_k_bills = get_needed_k_bills(drink)
    if needed_k_bills > k_doller_num:
        break

    current_drinks = [drink]
    while i < M - 1 and get_needed_k_bills(drinks[i + 1]) == needed_k_bills:
        current_drinks.append(drinks[i + 1])
        i += 1

    # 先頭から買うかどうか判断する
    for drink in current_drinks:
        if drink % K != 0:
            # おつりがもらえるなら、
            change = K - (drink % K)
            # おつりでデザートを買えるか判断し、買えるなら買う
            if desserts and desserts[-1] <= change + one_doller_num:
                answer += 2
                one_doller_num = one_doller_num + change - desserts[-1]
                desserts.pop()
                k_doller_num -= needed_k_bills
        else:
            answer += 1
            k_doller_num -= 1

    i += 1

print(answer)
