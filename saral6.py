import json
value = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
#print(value)
unique_value = json.loads(value)
print(unique_value) 

