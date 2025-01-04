A, B, C, D = map(int, input().split())

numbers: dict[int, int] = {}
if A in numbers:
    numbers[A] += 1
else:
    numbers[A] = 1
if B in numbers:
    numbers[B] += 1
else:
    numbers[B] = 1
if C in numbers:
    numbers[C] += 1
else:
    numbers[C] = 1
if D in numbers:
    numbers[D] += 1
else:
    numbers[D] = 1

if len(numbers) == 2:
    print("Yes")
else:
    print("No")
