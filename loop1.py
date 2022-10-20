alpha =[]
limit = int(input("Enter limit : "))
i=1
num=0
while i<=limit :
    print('Enter ',i, 'number')
    num = int(input())
    alpha.append(num)
    i+=1
print(alpha)
