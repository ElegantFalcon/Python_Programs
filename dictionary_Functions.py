
# ductionary is composed of keys and values

userdetail= { 1 : "Roy", 2: "Anirudh" , 3 : "Arjun"}
print(userdetail[1])
student = { "Name" : "Arjun", "Age": 18 , "Grade " : 12}
print(student["Age"])
alpha =  { 1 : "x", 2 : "y"}
print(student.values()) #Returns list of dictionary dict's values
alpha.clear() #Removes all elements of dictionary 
print(alpha) 
print("Shallow copy : " , student.copy())#Returns a shallow copy of dictionary dict
print("All keys of student :" ,student.keys()) #Returns list of dictionary dict's keys
userdetail.update(student) #	dict.update(dict2)Adds dictionary dict2's key-values pairs to dict
print("Update function : " , userdetail)
#print(student.has_key("Age")) REMOVED IN PYTHON 3
print(student.items()) #Returns a list of dict's (key, value) tuple pairs



#dict.copy()Returns a shallow copy of dictionary dict

print(userdetail.get(9, None))  #For key key, returns value or default if key not in dictionary

print(userdetail.setdefault(9, 'jhon')) #Similar to get(), but will set dict[key]=default if key is not already in dict



