iList = input("輸入一組四位數數字")
a = ""
swp = ""
swp1 = ""
for i in iList:
    a += str(int(i)+7 % 10)
    
swp = a[0]
swp1 = a[2]
a[0] = swp1
a[2] = swp

swp = a[1]
swp1 = a[3]
a[1] = swp1
a[3] = swp

print("加密後的數字為:",a)