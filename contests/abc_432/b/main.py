A = list(map(int, list(input())))
A.sort()
# print(A)
if A[0] == 0:
    non_zero_index = 0
    for i in range(len(A)):
        if A[i] != 0:
            non_zero_index = i
            break
    non_zero = A[non_zero_index]
    A = [non_zero] + A[:non_zero_index] + A[non_zero_index + 1 :]
# print(A)
print(int("".join([str(a) for a in A])))
