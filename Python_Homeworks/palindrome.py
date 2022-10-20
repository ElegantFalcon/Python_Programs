str = input("Enter a string : ")
str_reverse = str[::-1]
print("The reverse of the string is : " ,str_reverse)
if str == str_reverse : 
    print( str_reverse , " is a palindrome string ")
else : 
    print( str_reverse , " is not a palindrome string ")