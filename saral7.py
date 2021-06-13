# Text="Name, Abhishek, Designation, CEO of navgurukul, Gender, male, Age, 29"
# list1 = Text.strip('').split(', ')
# print ("final list", list1)
# import json
# name='dict.txt'
# d={ }
# with open(name) as f:
#     for line in f:
#         k,l = line.strip().split(None,1)
#         d[k]= l.strip()
# print(d)
# with open("dictking.json","w") as f:
#     json.dump(d,f,indent=4)
# f.close()

import  json
name='question7.txt'
d={}
with open(name) as f:
    for line in f:
        k,l = line.strip().split(None, 1) 
        d[k]=l.strip()
print(d)
with open("quik.json","w") as f:
    json.dump(d,f,indent=4)
f.close()




 