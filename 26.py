a = input("檢測的字串(end 結束)")

if a == "end":
    print("檢測結束")
else:
    b = input("檢測的字元:")
    numBeen = a.count(b)
    print("字元{}出現{}次".format(b, numBeen))