from collections import deque

S = list(input())

left_queue: deque[str] = deque()
# right_queue: deque[str] = deque()


def is_left(s):
    return s == "(" or s == "[" or s == "<"


def is_right(s):
    return s == ")" or s == "]" or s == ">"


def is_match(left, right):
    return (
        (left == "(" and right == ")")
        or (left == "[" and right == "]")
        or (left == "<" and right == ">")
    )


for s in S:
    if is_left(s):
        left_queue.append(s)
    if is_right(s):
        if not left_queue:
            print("No")
            exit()
        left = left_queue.pop()
        if not is_match(left, s):
            print("No")
            exit()
if left_queue:
    print("No")
else:
    print("Yes")
