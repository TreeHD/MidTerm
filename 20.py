numGroup = int(input("組數為:"))
for i in range(1, numGroup + 1):
    a, b = input("第{}組".format(i)).split(" ")
    print("第{}組應收費{}".format(i, int(a) *250 + int(b) * 175))
