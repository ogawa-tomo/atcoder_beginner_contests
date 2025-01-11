L, R = map(int, input().split())


# n桁のヘビ数の数
def n_digit_hebi(n):
    answer = 0
    for i in range(1, 10):
        answer += i ** (n - 1)
    return answer


# print(n_digit_hebi(3))


# Xの桁数で、X以上のヘビ数の数
def hebi_num_num_digits_more_than_or_equeal_num(X: int):
    # Xを桁数のリストで表す
    X_nums = [int(digit) for digit in str(X)]
    # Xの桁数
    X_digits = len(X_nums)
    answer = 0
    top_digit_num = X_nums[0]
    for num in range(top_digit_num + 1, 10):
        answer += num ** (X_digits - 1)
    for current_digit in range(X_digits - 1):
        # current_digit_num = X_nums[current_digit]
        next_digit_num = X_nums[current_digit + 1]
        if next_digit_num >= top_digit_num:
            break
        remaining_digits = X_digits - current_digit - 2
        for _ in range(next_digit_num + 1, top_digit_num):
            answer += top_digit_num**remaining_digits
        if current_digit + 1 == X_digits - 1 and next_digit_num < top_digit_num:
            answer += 1

    return answer


def is_hebi(X):
    X_nums = [int(digit) for digit in str(X)]
    # print(X_nums)
    top_digit_num = X_nums[0]
    for i, digit_num in enumerate(X_nums):
        if i == 0:
            continue
        if digit_num >= top_digit_num:
            return False
    return True


# Lを各桁のリストで表す
L_nums = [int(digit) for digit in str(L)]
# print(L_nums)
# Lの桁数
L_digits = len(L_nums)

R_nums = [int(digit) for digit in str(R)]
R_digits = len(R_nums)

answer = 0

# print(answer)
# print(n_digit_hebi(R_digits))
# print(hebi_num_num_digits_more_than_or_equeal_num(R))
if R_digits > L_digits:
    answer += hebi_num_num_digits_more_than_or_equeal_num(L)
    answer += n_digit_hebi(R_digits) - hebi_num_num_digits_more_than_or_equeal_num(R)
    if is_hebi(R):
        answer += 1
if R_digits == L_digits:
    answer += hebi_num_num_digits_more_than_or_equeal_num(
        L
    ) - hebi_num_num_digits_more_than_or_equeal_num(R)
    if is_hebi(R):
        answer += 1
# print(answer)
for digit in range(L_digits + 1, R_digits):
    answer += n_digit_hebi(digit)
print(answer)

# print(n_digit_hebi(3))
# print(hebi_num_num_digits_more_than_or_equeal_num(210))
# print(hebi_num_num_digits_more_than_or_equeal_num(211))
# print(is_hebi(5512))
