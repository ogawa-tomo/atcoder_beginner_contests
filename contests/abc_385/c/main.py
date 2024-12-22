N = int(input())
H = list(map(int, input().split()))

answer = 1

# for i in range(N):
#     # i番目のビルの高さを選ぶケース

#     num = 1
#     height = H[i]
#     aida = 1
#     index = i
#     while True:
#         index += aida
#         if H[index] == height:


for aida in range(1, N):
    # 間隔がaidaのケース
    for amari in range(aida):
        # aidaで割った余りがamariを選ぶケース
        num = 1
        index = amari
        height = H[amari]
        while True:
            index += aida
            if index >= N:
                break
            if H[index] == height:
                num += 1
            else:
                answer = max(num, answer)
                num = 1
                height = H[index]
        answer = max(num, answer)


# for i in range(N):
#     # i番目のビルを選ぶケース
#     height = H[i]
#     for aida in range(1, N - i + 1):
#         # 間隔がaidaのケース
#         num = 1
#         condition = True
#         index = i + aida
#         while index < N:
#             num += 1
#             if H[index] != height:
#                 condition = False
#                 break
#             index += aida
#         if condition:
#             answer = max(num, answer)

print(answer)
