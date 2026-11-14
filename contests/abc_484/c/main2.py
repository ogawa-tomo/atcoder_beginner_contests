# AC
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def is_ok(A: list[int], B: list[int]):
    ai = 0
    bi = 0
    needed_a = 0
    a_slided = False
    b_slided = False
    while ai < N and bi < N:
        a = A[ai]
        b = B[bi]
        # print(a, b)

        if a == b:
            ai += 1
            bi += 1
            continue

        if not b_slided:
            b_slided = True
            needed_a = b
            bi += 1
            if bi >= N:
                return False
                # ok = False
                # break
            continue

        if a_slided:
            return False
            # ok = False
            # break
        # 異なる値で、Aはまだスライドしてない
        if a != needed_a:
            return False
            # ok = False
            # break
        a_slided = True
        ai += 1

    # print(b_slided, a_slided)
    if b_slided and not a_slided:
        return needed_a == A[-1]
    return True


ok1 = is_ok(A, B)
A.reverse()
B.reverse()
ok2 = is_ok(A, B)

# print(ok1, ok2)
if ok1 or ok2:
    print("Yes")
else:
    print("No")
