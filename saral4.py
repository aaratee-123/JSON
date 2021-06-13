import json
number={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
num=open("num_file.json","w")
json.dump(number,num, sort_keys=True,indent=6)
num.close()

