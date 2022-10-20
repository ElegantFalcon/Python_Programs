def fibo(limit) :
    a = 0
    b = 1 
    print (a)
    print(b)
    for i in range(0 ,limit ) :
        c = a + b
        print(c)
        a = b 
        b = c 

lim = int(input("Emter limit : "))
fibo(lim)