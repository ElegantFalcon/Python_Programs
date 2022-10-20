
counts = dict()
names = ['csev', 'cwen' , 'csev' , 'zqian', 'cwen']
for name in names : 
    counts[name] = counts.get(name , 0) + 1  #we can use get() and rovide a default value of zero when the key is
                                             #yet not in the dictionary- and then just add one
print(counts)




#using get is equivalent to the following code
"""
counts = dict()
names = ['csev', 'cwen' , 'csev' , 'zqian', 'cwen']
for name in names : 
    if name not in counts :
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
"""
