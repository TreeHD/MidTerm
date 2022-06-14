a = input("找出字串重複的字")
d = {}
g = []

for i in a:
    if(i in d):
        d[i] += 1
    else:
        d[i] = 1

for k,v in d.items():
    if(v > 1):
        g.append(k)

print(g)