import math

score = []

score.append(int(input("國文")))
score.append(int(input("英文")))
score.append(int(input("微積分")))
score.append(int(input("體育")))
score.append(int(input("程式設計")))
sub = {0: "國文", 1: "英文", 2: "微積分", 3: "體育", 4: "程式設計"}
total = round(sum(score)/5, 3)
minium = min(score)
maxium = max(score)


print("平均分數", total)
print("最高分科目", sub[score.index(maxium)], maxium)
print("最低分科目", sub[score.index(minium)], minium)
