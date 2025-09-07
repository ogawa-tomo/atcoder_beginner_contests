# どうしてWAなのか分からねぇ…
T = int(input())
for _ in range(T):
    na, nb, nc = map(int, input().split())
    min_ac = min(na, nc)
    max_ac = max(na, nc)
    # residue = max_ac - min_ac + nb
    # if residue >= min_ac:
    #     print(min_ac)
    # else:
    abc_num = min(min_ac, nb)
    na -= abc_num
    nc -= abc_num
    nb -= abc_num

    if nb == 0:
        min_ac = min(na, nc)
        max_ac = max(na, nc)
        aac_or_acc_num = min(max_ac // 2, min_ac)
        max_ac -= aac_or_acc_num // 2
        min_ac -= aac_or_acc_num
        if max_ac == 1 and min_ac >= 2:
            aac_or_acc_num += 1
        print(abc_num + aac_or_acc_num)
        continue
    else:
        print(abc_num)
