K = int(input())
S = list(input())
T = list(input())

# if S == T:
#     print("Yes")
#     exit()

# 操作1：Sに1文字挿入
if len(S) + 1 == len(T):
    wrong = 0
    s_index = 0
    t_index = 0
    while s_index < len(S):
        if S[s_index] != T[t_index]:
            wrong += 1
            if wrong > 1:
                print("No")
                exit()
            if S[s_index] != T[t_index + 1]:
                print("No")
                exit()
            s_index += 1
            t_index += 2
        else:
            s_index += 1
            t_index += 1
    print("Yes")
    exit()

# 操作2：Sから1文字削除
if len(T) + 1 == len(S):
    wrong = 0
    s_index = 0
    t_index = 0
    while t_index < len(T):
        if T[t_index] != S[s_index]:
            wrong += 1
            if wrong > 1:
                print("No")
                exit()
            if T[t_index] != S[s_index + 1]:
                print("No")
                exit()
            t_index += 1
            s_index += 2
        else:
            s_index += 1
            t_index += 1
    print("Yes")
    exit()

# 操作3：1文字変換
if len(S) == len(T):
    wrong = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            wrong += 1
            if wrong > 1:
                print("No")
                exit()
    print("Yes")
    exit()

print("No")
# # 操作1：Sに1文字挿入
# if len(S) + 1 == len(T):
#     for i in range(len(T)):
#         # print(S[:i], S[i:])
#         # print(T[:i], T[i + 1 :])
#         if S[:i] == T[:i] and S[i:] == T[i + 1 :]:
#             print("Yes")
#             exit()

# # 操作2：Sから1文字削除
# if len(S) == len(T) + 1:
#     for i in range(len(S)):
#         # print(S[:i], S[i + 1 :])
#         # print(T[:i], T[i:])
#         if S[:i] == T[:i] and S[i + 1 :] == T[i:]:
#             print("Yes")
#             exit()

# # 操作3：1文字変換
# if len(S) == len(T):
#     for i in range(len(S)):
#         # print(S[:i], S[i + 1 :])
#         # print(T[:i], T[i + 1 :])
#         if S[:i] == T[:i] and S[i + 1 :] == T[i + 1 :]:
#             print("Yes")
#             exit()

# print("No")
