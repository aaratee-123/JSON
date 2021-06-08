#python object convert json string
import json
name={'arti':'akola','rashi':'nashik'}
print(name)
print(type(name))
shell=open("task_file.json","r")
y=json.dumps(name)
print(y)
print(type(y))

