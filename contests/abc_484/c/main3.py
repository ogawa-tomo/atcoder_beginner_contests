# AC
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


while A and B and A[-1] == B[-1]:
    A.pop()
    B.pop()

A.reverse()
B.reverse()
while A and B and A[-1] == B[-1]:
    A.pop()
    B.pop()

if not A and not B:
    print("Yes")
    exit()

# 左巡回シフト
A1 = A[1:]
A1.append(A[0])
# 右巡回シフト
A2 = [A[-1]]
A2.extend(A)
A2.pop()

# print(A1)
# print(A2)
# print(B)

if A1 == B or A2 == B:
    print("Yes")
else:
    print("No")
