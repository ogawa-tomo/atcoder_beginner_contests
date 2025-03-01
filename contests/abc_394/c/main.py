S = list(input())

# length = len(S)
# for i in range(length - 1):
#     if S[i] == 'W' and S[i + 1] == 'A':
#         prev = i - 1
#         while prev >= 0:


in_w_zone = False
w_start_index = 0
w_end_index = 0
w_start_end_list: list[list[int]] = []
for i, s in enumerate(S):
    if s == "W":
        if in_w_zone:
            continue
        in_w_zone = True
        w_start_index = i
    elif s == "A" and in_w_zone:
        w_end_index = i
        w_start_end_list.append([w_start_index, w_end_index])
        in_w_zone = False
    else:
        in_w_zone = False

for w_start_end in w_start_end_list:
    w_start_index = w_start_end[0]
    w_end_index = w_start_end[1]
    S[w_start_index] = "A"
    for i in range(w_start_index + 1, w_end_index + 1):
        S[i] = "C"
print("".join(S))
