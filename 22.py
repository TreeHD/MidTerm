dataset = {"123": {"password": "456", "money": "9000"}, "456": {"password": "789", "money": "5000"}, "789": {"password": "888", "money": "6000"},
           "336": {"password": "558", "money": "10000"}, "775": {"password": "666", "money": "12000"}, "566": {"password": "221", "money": "7000"}}

numArray = int(input("輸入查詢數組N為:"))

for i in range(numArray):
    a, b = input("").split(" ")
    if a in dataset:
        if b == dataset[a]["password"]:
            print(dataset[a]["money"])
        else:
            print("ERROR")
    else:
        print("ERROR")
