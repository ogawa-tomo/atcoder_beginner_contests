N = int(input())
A = list(map(int, input().split()))

num_of_people: dict[int, int] = {}

current_max = 0

answer = -1
for a in A:
    if a in num_of_people:
        num_of_people[a] += 1
    else:
        num_of_people[a] = 1

# print(num_of_people)
for i, a in enumerate(A):
    if num_of_people[a] == 1 and a > current_max:
        current_max = a
        answer = i + 1

print(answer)
