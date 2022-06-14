a = {}

n = int(input("輸入筆數"))
for i in range(n):
    tmp = input().split()
    a[tmp[0]] = tmp[1]

q = input("輸入要查詢的字串:")
if q in a:
    print(q, "中文是", a[q])

