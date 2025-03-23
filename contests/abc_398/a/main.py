N = int(input())

if N == 1:
    print("=")
    exit()

if N == 2:
    print("==")
    exit()

answer: list[str] = []

if N % 2 == 0:
    num_hyphen = (N - 2) // 2
    for _ in range(num_hyphen):
        answer.append("-")
    answer.extend(["=", "="])
    for _ in range(num_hyphen):
        answer.append("-")
    print("".join(answer))
    exit()

else:
    num_hyphen = (N - 1) // 2
    for _ in range(num_hyphen):
        answer.append("-")
    answer.append("=")
    for _ in range(num_hyphen):
        answer.append("-")
    print("".join(answer))
    exit()
