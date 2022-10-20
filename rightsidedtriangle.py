limit =5
for i in range(0, limit) : 
    for j in range(i, limit): 
        print(' ', end=' ') 
    for j in range(i+1): 
        print('* ', end='') 

    print('\r') 

print("---------------------")
lim =5
for i in range(0, lim) : 
    for j in range(i+1): 
        print(' ', end=' ') 
    for j in range(i , lim): 
        print('* ', end='') 

    print('\r') 