# Q1) Find the length of the given string (without using built in functions)
str = input("Enter a string : ")
word_count = 0
for i in str :
    word_count = word_count + 1

print( "The number of words in the string is : " , word_count)