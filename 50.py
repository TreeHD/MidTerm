allStu = set(['John', 'Mary', 'Tina', 'Fiona',
             'Claire', 'Eva', 'Ben', 'Bill', 'Bert'])
engPass = set(['John', 'Mary', 'Fiona', 'Claire', 'Ben', 'Bill'])
mathPass = set(['Mary', 'Fiona', 'Claire', 'Eva', 'Ben'])

print("英文數學都及格", engPass & mathPass)
print("數學不及格", allStu-mathPass)
print("英文及格且數學不及格", engPass & (allStu-mathPass))
