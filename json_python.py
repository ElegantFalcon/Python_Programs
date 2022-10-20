import json
pyth_dict = {'name': 'nik', 'id': 54, 'address': 'calicut ', 'completed': False}
with open("jsonfile2.json" , "w")  as st :
    json.dump(pyth_dict , st)


# import json
# pyth_dict = {'name': 'nik', 'id': 543, 'address': 'calicut ', 'completed': False}
# ##json_str = json.dumps(pyth_dict)
# #print(json_str)