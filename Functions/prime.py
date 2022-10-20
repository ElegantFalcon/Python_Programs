def prime(num) :
    count = 0
    for i in range (1 , num ) :
        if num % i == 0 :
            count = count + 1
        else:
            pass
    if count == 1:
        print(num , " is a prime number")
    else :
        print(num , " is a not prime number")

    
n = int(input("Enter a number : "))
prime(n)


    
