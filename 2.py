# 電費計算
def summer(electricity):
    layer2 = 120*2.10
    layer3 = layer2 + 210 * 3.02
    layer4 = layer3 + 170 * 4.39
    layer5 = layer4 + 200 * 4.97

    if electricity <= 120:
        print("夏月電費為：", 2.10*electricity)
    elif electricity > 120 and electricity <= 330:
        print("夏月電費為：", layer2+(electricity-120)*3.02)
    elif electricity > 330 and electricity <= 500:
        print("夏月電費為：", layer3+(electricity-330)*4.39)
    elif electricity > 500 and electricity <= 700:
        print("夏月電費為：", layer4+(electricity-500)*4.97)
    else:
        print("夏月電費為:", layer5+(electricity-700)*5.63)


def nosunner(electricity):
    layer2 = 120*2.10
    layer3 = layer2 + 210 * 2.68
    layer4 = layer3 + 170 * 3.61
    layer5 = layer4 + 200 * 4.01

    if electricity <= 120:
        print("非夏月電費為：", 2.10*electricity)
    elif electricity > 120 and electricity <= 330:
        print("非夏月電費為：", layer2+(electricity-120)*2.68)
    elif electricity > 330 and electricity <= 500:
        print("非夏月電費為：", layer3+((electricity-330)*3.61))
    elif electricity > 500 and electricity <= 700:
        print("非夏月電費為：", layer4+((electricity-500)*4.01))
    else:
        print("非夏月電費為:", layer5+((electricity-700)*4.50))


electricity = int(input("請輸入用電度數："))
nosunner(electricity)
summer(electricity)
