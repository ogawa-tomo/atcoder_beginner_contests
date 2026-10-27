# x以下の素数列挙
def sieve_of_eratosthenes(x: int):
    nums = [i for i in range(x + 1)]

    root = int(pow(x, 0.5))
    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x + 1):
                if i * j >= x + 1:
                    break
                nums[i * j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


S = input()

digits = len(S)
primes = sieve_of_eratosthenes(int("9" * digits))

for prime in primes:
    T = str(prime)
    if len(T) != digits:
        continue

    ok = True
    for i in range(digits - 1):
        si = S[i]
        ti = T[i]
        for j in range(i, digits):
            sj = S[j]
            tj = T[j]

            if (si == sj and ti != tj) or (ti == tj and si != sj):
                ok = False
                break
        if not ok:
            break

    if ok:
        print(prime)
        exit()

print(-1)
