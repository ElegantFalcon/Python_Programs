def primesum(num) :
    prime=[]
    count = 0
    for i in range (1 , num ) :
        if num % i == 0 :
            count = count + 1
        if count == 1:
            prime.append[num]

    print(prime)
    
n = int(input("Enter  a number : "))
primesum(n)