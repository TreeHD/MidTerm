a = input("請輸入傳送密碼(6位數)")
data = ""
for i in a:
    for j in range(0, 10):
        if(j*4 % 7 == int(i)):
            data += str(j)
            break

print("解密後的密碼",data)
