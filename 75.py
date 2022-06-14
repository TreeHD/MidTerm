todo = []

i = ""
k = 0
while i != "end":
    i = input("輸入代辦事項(沒有打end)")
    todo.append(i)

for v in todo:
    k += 1
    print("{}.{}".format(k, v))
