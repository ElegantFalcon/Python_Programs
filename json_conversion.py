#------- Strig conversion

# import json
# json_str = '{"name" :  "nik" , "subject" : "cs" , "age " : 18 }'
# print(json_str)
# print(json_str[0])
# python_dict = json.loads(json_str)
# print(python_dict)

import json
with open ('jsonfile.json') as file : 
    python_dict = json.load(file)

print(python_dict['title'])