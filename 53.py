n = int(input("輸入n值"))
a = 0
data = []

for i in range(n):
    name = input("輸入姓名:")
    email = input("輸入email:")
    tmp = {"name": name, "email": email}
    data.append(tmp)
q = input("輸入要查詢的姓名:")

for i in data:
    if i["name"] == q:
        print(q,"的電子郵件為",i["email"])
        a = 1



