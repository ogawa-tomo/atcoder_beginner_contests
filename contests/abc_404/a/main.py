S = list(input())

alphabets = list("abcdefghijklnmopqrstuvwxyz")

for s in S:
    for i, alphabet in enumerate(alphabets):
        if s == alphabet:
            alphabets.pop(i)

print(alphabets[0])
