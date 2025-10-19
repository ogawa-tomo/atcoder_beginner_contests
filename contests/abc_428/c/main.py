from collections import deque

S: deque[str] = deque()

# needed_right_num:[n]: n番目の文字まであるとき、カッコ閉じがいくつ必要か
needed_right_nums: deque[int | None] = deque()

Q = int(input())
for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        c = query[1]
        if len(needed_right_nums) == 0:
            print("No")
            if c == "(":
                needed_right_nums.append(1)
                continue
            if c == ")":
                needed_right_nums.append(None)
                continue
        last_needed_right_num = needed_right_nums[-1]
        if last_needed_right_num is None:
            print("No")
            needed_right_nums.append(None)
            continue
        if c == "(":
            print("No")
            needed_right_nums.append(last_needed_right_num + 1)
            continue
        if c == ")":
            if last_needed_right_num == 0:
                print("No")
                needed_right_nums.append(None)
            if last_needed_right_num > 0:
                next_needed_right_num = last_needed_right_num - 1
                if next_needed_right_num == 0:
                    print("Yes")
                else:
                    print("No")
                needed_right_nums.append(next_needed_right_num)
    else:
        # print("hoge")
        needed_right_nums.pop()
        if len(needed_right_nums) == 0:
            print("Yes")
        else:
            if needed_right_nums[-1] == 0:
                print("Yes")
            else:
                print("No")
