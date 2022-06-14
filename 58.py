a= []
for i in range(10):
    a.append(int(input("輸入第"+str(i+1)+"個數字")))

a.sort()
print("最大的3個數字", a[-3:])
print("最小的3個數字", a[:3])
