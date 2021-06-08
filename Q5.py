import json
name='{"arti":"akola","rashi":"nashik"}'
f = open('data.json',"w")
   
data = json.load(f)
   
for i in data[name]:
    print(i)
   
f.close()