pswd = "1234"
guess = None
count = 0

while pswd != guess :
    guess = input("enter password")
    if pswd == guess :
        print ("login success")
        break
    else :
        count += 1 

        print("Incorrect password, Try again!!")
        if count == 3:
            print ("Too many attempts!!Try again later")
            break 