def char_str(str, chr) :
    str2 = str.replace(chr , "")
    print("The string : " , str , "  after replacing " , chr , " is : " , str2)


a = input("Enter a string :")
b = input("Enter the character to be removed : ")
char_str(a , b)

