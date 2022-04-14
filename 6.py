a = input("輸入值為:").split(",")

minArr = sorted(a)
maxArr = sorted(a, reverse=True)
min = ""
max = ""
for i in maxArr:
    max += (i)
for i in minArr:
    min += (i)

print(int(max) - int(min))
