email = "qwer@gmail.com"
pswd = "1234"

einput = input("enter your email : ")

if einput == email :
    pinput = input("Enter your pswd : ")
    if pinput == pswd :
        print("Login Successful")
    else :
        print("Wrong password!!")
else : 
    print("Login failed!!")
    
