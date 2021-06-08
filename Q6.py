import json
name='{"arti":"akola","rashi":"nashik"}'
shell=open("t.json","a")
y=json.loads(name)
print(y)
#name.close()