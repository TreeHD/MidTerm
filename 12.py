a = input("輸入正數序列: ").split(" ")
b = []

for i in a:
    b.append(a.count(i))

toindex = b.index(max(b))

if max(b) > len(a) / 2:
    print("過半元素為YES")
else:
    print("過半元素為NO")
