km = float(input("輸入公里數(km):"))
m = km * 1000
if(km < 1.5):
    res = 75
else:
    if(m % 250 != 0):
        res = 75+(int((m-1500)/250)*5) + 5
    else:
        res = 75+(int((m-1500)/250)*5)


print("所需車資為:", res)
