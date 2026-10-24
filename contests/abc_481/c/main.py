Q = int(input())

id = 1
account_id_by_name: dict[str, int] = dict()
for _ in range(Q):
    s = input()
    if s in account_id_by_name:
        print(account_id_by_name[s])
    else:
        account_id_by_name[s] = id
        print(id)
        id += 1
