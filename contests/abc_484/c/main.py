# WA
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ai = 0
bi = 0
needed_a: int | None = None
swapped = False
ok1 = True
while ai < N and bi < N:
    a = A[ai]
    b = B[bi]

    if a == b:
        ai += 1
        bi += 1
        continue

    if needed_a is None:
        # bを探して挿入する必要がある
        needed_a = b
        # aiは足さない
        bi += 1
        continue

    if not swapped and a == needed_a:
        ai += 1
        # biは足さない
        swapped = True
        continue

    ai += 1
    bi += 1

if needed_a is not None:
    if swapped:
        ok1 = True
    else:
        ok1 = False
else:
    ok1 = True

ai = 0
bi = 0
needed_a: int | None = None
swapped = False
ok2 = True
A.reverse()
B.reverse()
while ai < N and bi < N:
    a = A[ai]
    b = B[bi]

    if a == b:
        ai += 1
        bi += 1
        continue

    if needed_a is None:
        # bを探して挿入する必要がある
        needed_a = b
        # aiは足さない
        bi += 1
        continue

    if not swapped and a == needed_a:
        ai += 1
        # biは足さない
        swapped = True
        continue

    ai += 1
    bi += 1
    # ok2 = False
    # break

if needed_a is not None:
    if swapped:
        ok2 = True
    else:
        ok2 = False
else:
    ok2 = True
print(ok1, ok2)
if ok1 or ok2:
    print("Yes")
else:
    print("No")
