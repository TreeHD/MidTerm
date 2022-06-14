import random
import math
guess = ""


for i in range(4):
    guess += (str(math.floor(random.uniform(1, 10))))

inp = ""
while inp != guess and inp != "0":
    result = {"A": 0, "B": 0}
    inp = input("輸入數字")

    for i in range(4):
        if inp[i] == guess[i]:
            result["A"] += 1
        elif inp[i] in guess:
            result["B"] += 1

    print(result["A"], "A", result["B"], "B")
