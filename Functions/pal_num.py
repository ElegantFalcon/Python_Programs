def palindrome(num) : 
    reverse = num[::-1]
    if num == reverse :
        print(num , " is a palindrome number")
    else :
        print(num , " is not a palindrome number")

n = str(input("Enter a number : "))
palindrome(n)
