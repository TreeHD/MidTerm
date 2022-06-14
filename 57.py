price = [0, 72, 62, 82, 44, 60]

a = input("請選擇主餐+升級套餐")
b = input("是否升級為大杯飲料")
c = input("是否換成大薯")

r = price[int(a[0])]

if(a[1] == "A"):
    r += 55
elif(a[1] == "B"):
    r += 68

if b == "是":
    r += 7
if c == "是":
    r += 13

print("總計", r)
