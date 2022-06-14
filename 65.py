a = set()
b = set()

a.add()

ai = input("輸入A的好友").split(" ")
bi = input("輸入B的好友").split(" ")

for i in ai:
    a.add(i)

for i in bi:
    b.add(i)

print(len(a & b))