a = input("輸入月租費以及通話時間").split(",")
fee = int(a[0])
time = int(a[1])

totalFee = 0

if fee == 186:
    base = 186
    rate = 0.09
    if time > round(base/rate):
        if time > round(base/rate)*2:
            totalFee = base + (time - round(base/rate))*(rate*0.8)
        else:
            totalFee = base + (time - round(base/rate))*(rate*0.9)
    else:
        totalFee = fee

elif fee == 386:
    base = 386
    rate = 0.08
    if time > round(base/rate):
        if time > round(base/rate)*2:
            totalFee = base + (time - round(base/rate))*(rate*0.7)
        else:
            totalFee = base + (time - round(base/rate))*(rate*0.8)
    else:
        totalFee = fee
elif fee == 586:
    base = 586
    rate = 0.07
    if time > round(base/rate):
        if time > round(base/rate)*2:
            totalFee = base + (time - round(base/rate))*(rate*0.6)
        else:
            totalFee = base + (time - round(base/rate))*(rate*0.7)
    else:
        totalFee = fee
elif fee == 986:
    base = 986
    rate = 0.06
    if time > round(base/rate):
        if time > round(base/rate)*2:
            totalFee = base + (time - round(base/rate))*(rate*0.5)
        else:
            totalFee = base + (time - round(base/rate))*(rate*0.6)
    else:
        totalFee = fee

print("通話費為{}".format(round(totalFee)))
