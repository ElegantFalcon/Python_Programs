def lcm(a, b):

    if a > b:
       great_num = a
    else:
       great_num = b
    
    while(True):
       if((great_num % a == 0) and (great_num % b == 0)):
           result = great_num
           break
       great_num = great_num + 1
    print("The LCM of " , a , " and " , b , " is : " , result)

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
lcm(num1 , num2)