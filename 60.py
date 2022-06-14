a = "aeiou"

b = input("輸入一串小寫英文")
res = ""
for i in b:
    if i in a:
        res+="."
    else:
        res+=i

print(res)
