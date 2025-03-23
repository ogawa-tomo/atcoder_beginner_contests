# これはWA
A = list(map(int, input().split()))

cards_3 = False
cards_2 = False
cards_2_nums: set[int] = set()
card_dict: dict[int, int] = {}
for a in A:
    if a not in card_dict:
        card_dict[a] = 1
    else:
        card_dict[a] += 1
    if card_dict[a] == 2:
        cards_2_nums.add(a)
    if card_dict[a] == 3 and len(cards_2_nums) > 1:
        print("Yes")
        exit()

# print(cards_2_nums)
print("No")
