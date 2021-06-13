f= open("pooja.txt","r")
data = f.read()
txt=data
x=txt.split()
dict1={}
i=0
while i<len(x)-1:
    new_dic={x[i]:x[i+1]}
    dict1.update(new_dic)
    i=i+2
print(dict1)
import json
file =open("text.json","w")
json.dump(dict1,file,indent=6)
file.close()