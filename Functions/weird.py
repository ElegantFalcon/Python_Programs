def weird(num):
    if num % 2 != 0 :
        print ("weird Number !!")
    elif num % 2 == 0 and 2<num<5 :
        print("Not weird")
    elif num % 2 == 0 and 6<num<20 :
        print("Weird Number !!")
    elif num % 2 == 0 and num >20 :
        print("Not weird")
    else :
        print("Wrong input !!!!")

n = int(input("Enter a number: "))
weird(n)

    
