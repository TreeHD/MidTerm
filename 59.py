pr = int(input(""))

y100 = pr//100
y100s = pr%100

y50 = y100s//50
y50s = y100s%50

y10 = y50s//10
y10s = y50s%10

y5 = y10s//5
y5s = y10s%5

y1 = y5s//1



print(y100+y50+y10+y5+y1)