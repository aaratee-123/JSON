import simplejson as json


em1=["neelam","programer","24","2400"]
em2=["komal","trainer","24","20000"]
em3=["anuradha","HR","25","40000"]
em4=["Abhishek","manager","29","63000"]  
k=["name","designation","age","salary"]
m=["emp1","emp2","emp3","emp4"]

emp1={}
emp2={}
emp3={}
emp4={}
dict1=[]
main_dict={}
for key in k:
    for value in em1:
        emp1[key]=value
        em1.remove(value)
        break
dict1.append(emp1)
# print("emp1:-",emp1)
for key in k:
    for value in em2:
        emp2[key]=value
        em2.remove(value)
        break
dict1.append(emp2)
# print("emp2:-",emp2)
for key in k:
    for value in em3:
        emp3[key]=value
        em3.remove(value)
        break
dict1.append(emp3)
# print("emp3:-",emp3)
for key in k:
    for value in em4:
        emp4[key]=value
        em4.remove(value)
        break
dict1.append(emp4)
# print("emp4:-",emp4)
print("dict1:- ",dict1)
print()
for key in m:
    for value in dict1:
        main_dict[key]=value
        dict1.remove(value)
        break
print("maindict:-",main_dict)

with open ("employee.json","w") as f:
    json.dump(main_dict,f,indent=4)
f.close()