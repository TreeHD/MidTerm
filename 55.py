a = ['飢餓遊戲3']
b = ['房思琪的初戀樂園']
r = input("輸入要租借的書")
exist = 0
i = 0
if r in a:
    exist = a
    i = a.index(r)
if r in b:
    exist = b
    i = a.index(r)

if exist == 0:
    print("沒有這本書")
else:
    print("在書架{}的第{}本".format(exist, i))
