# ACだったりTLEだったりする
A = int(input())
N = int(input())


# nの桁数
def digits(n, base):
    i = 0
    while True:
        if n < base**i:
            return i
        i += 1


# nを分解する
def divide(n: int, base: int):
    number = n
    result: list[int] = []
    digits_num = digits(n, base)
    for d in range(digits_num):
        digit = base ** (digits_num - d - 1)
        digit_num = number // digit
        result.append(digit_num)
        number -= digit * digit_num

    return result


def restore(n: list[int], base: int):
    result = 0
    len_n = len(n)
    for i in range(len_n):
        result += n[i] * (base ** (len_n - i - 1))
    return result


def is_palindrome(n: int, base: int):
    divided_n = divide(n, base)
    for i in range(len(divided_n) // 2):
        if divided_n[i] != divided_n[len(divided_n) - i - 1]:
            return False
    return True


# nが回文数のとき、nの次の回文数
def next_palindrome(n: list[int]):
    len_n = len(n)
    if len_n == 1:
        if n[0] == 9:
            return [1, 1]
        else:
            return [n[0] + 1]
    if len_n == 2:
        if n[0] == 9:
            return [1, 0, 1]
        else:
            return [n[0] + 1, n[0] + 1]
    all_nine = True
    for d in range(1, len_n - 1):
        if n[d] != 9:
            all_nine = False
            break
    if all_nine:
        if n[0] == 9:
            return [1, *[0] * (len_n - 1), 1]
        else:
            return [n[0] + 1, *[0] * (len_n - 2), n[0] + 1]
    return [n[0], *next_palindrome(n[1 : len_n - 1]), n[0]]


n = 1
answer = 0
while n <= N:
    if is_palindrome(n, A):
        answer += n
    n = restore(next_palindrome(divide(n, 10)), 10)

print(answer)
