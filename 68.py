guess = input("輸入數字A")


inp = input("輸入數字B")

result = {"A": 0, "B": 0}
for i in range(len(guess)):
    if inp[i] == guess[i]:
        result["A"] += 1
    elif inp[i] in guess:
        result["B"] += 1

if(result["A"] == 4):
    print(result["A"], "A", result["B"], "B","全對")
else:
    print(result["A"], "A", result["B"], "B","加油")