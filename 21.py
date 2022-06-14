dataset = {"123":{'name':'Tom', 'subjet':'DTGD'},"456":{'name':'Cat', 'subjet':'CSIE'},"789":{'name':'Nana', 'subjet':'ASIE'},"321":{'name':'Lim', 'subjet':'DBA'},"654":{'name':'Won', 'subjet':'FDD'}}
i = input("Enter your student ID: ")
print(i,dataset[i]["name"],dataset[i]["subjet"])