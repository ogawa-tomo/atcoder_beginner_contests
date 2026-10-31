S = input()

count = 0
for s in S:
    if s == "o":
        count += 1

if count % 2 == 1:
    print("odd")
else:
    print("even")
