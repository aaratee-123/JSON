import simplejson as json
x={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
#print(type(x))
with open("shopping.json","w")as f:
    json.dump(x,f,indent=4)
name=input("which you want to buy")
items=int(input("how many items you want"))
for keys in x:
    for value in x:
        for i,k in x[keys].items():
            #print(i,k)
            if i==name:
                t=int(k)-items
                print(t)

