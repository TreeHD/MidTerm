m = int(input())
d = int(input())
r = {0: "普通", 1: "吉", 2: "大吉"}
s = (m*2+d) % 3
print(r[s])
