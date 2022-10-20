def prime(num1 , num2) :
    sum = 0
    count = 0
    for i in range (num1  , num2 ) :
        if num1 % i == 0 :
            count = count + 1
        else :
            pass
        if count == 1:
            sum = sum + num1
            print(sum)
        else :
            pass
        num1 = num1 + 1

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
prime(n1 , n2)