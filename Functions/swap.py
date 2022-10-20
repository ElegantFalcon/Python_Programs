def swap(a , b) : 
    print ("Values before swap")
    print ("Number 1 :" , a)
    print ("Number 2 :" , b)
    a = a + b
    b = abs(a-b)
    a = a - b
    print ("Values after swap")
    print ("Number 1 :" , a)
    print ("Number 2 :" , b)
    

num1 = int(input("Enter First number : "))
num2 = int(input("Enter second Number : "))
swap( num1 , num2)

