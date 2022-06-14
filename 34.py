a = int(input("輸入一數字"))
if a % 2 == 0 and a % 11 == 0 and a % 5 != 0 and a % 7 != 0:
    print(a, "是新公倍數嗎: yes")
else:
    print(a, "是新公倍數嗎: no")
