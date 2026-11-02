N = int(input())
C = list(map(int, input().split()))

num_by_color = [0] * (N + 1)
for c in C:
    num_by_color[c] += 1

print(N - max(num_by_color))
