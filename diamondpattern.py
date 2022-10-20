limit = 5
for i in range(limit):

    for j in range(i , limit):
        print(' ' , end = ' ')

    for j in range(i):
        print('*' , end = ' ')

    for j in range(i+1):
        print('*' , end =' ')

    print()


limit = 5
for i in range(limit):

    for j in range(i+1):
        print(' ' , end = ' ')

    for j in range(i , limit-1):
        print('*' , end = ' ')

    for j in range(i, limit):
        print('*' , end =' ')

    print()

