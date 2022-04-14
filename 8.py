n = int(input("輸入第一行正整數為"))
a = input("輸入第二行數列的中的數字").split(" ")
b = []


for i in a:
    b.append(a.count(i))


toindex = b.index(max(b))
if max(b) == 1:
    print("沒有重複數字")
else:
    print("最大出現次數為:{},出現次數為:{}".format(a[toindex],max(b)))