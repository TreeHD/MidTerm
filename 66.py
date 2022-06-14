
a = set()
b = set()
r = []
sa = input("輸入string_a")
sb = input("輸入string_b")

for i in sa:
    a.add(i)
for i in sb:
    b.add(i)

for i in a & b:
    r.append(i)
r.sort()


print(r)
