def fact(lim) :
    product = 1
    for i in range(1, lim+1):
        product = product * i
    
    print(product)

num = int(input("Enter a number : "))
fact(num)

