import json
with open ('fake_api_json.json') as trial : 
    python_dict = json.load(trial)
#print(python_dict)
for i in range(0, 5) :
    print("Id :",python_dict[i]['id'] ,  "------" , "Title : " , python_dict[i]['title'])
