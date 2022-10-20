def hcf(a, b):
    if a > b:
        small_num = b
    else:
        small_num = a
    for i in range(1, small_num+1):
        if((a % i == 0) and (b % i == 0)):
            ans = i 
    print("HCF of " ,a , " and " , b, " is : " , ans)

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
hcf(num1 , num2)
