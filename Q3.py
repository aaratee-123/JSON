#1-creat json file from dictionary
import json
name={'arti':'akola','rashi':'nashik'}
shell=open("task_file.json","w")
y=json.dump(name,shell)
#print(y)
#shell.close()
#name.closed()
# parsed_json = (json.loads(json_data))
# print(json.dumps(parsed_json, indent=4, sort_ke