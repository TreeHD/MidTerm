a = int(input("輸入筆數"))
r = []
r1 = ["金", "銀", "銅", "優"]

for i in range(a):
    r.append(int(input(r1[i])))

for i in range(a):
    print(r1[i], "牌有", r[i])
