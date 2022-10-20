str = input("Enter a string : ")
count_l = 0
count_u = 0
for i in str:
      if(i.islower()):
            count_l = count_l + 1
      elif(i.isupper()):
            count_u = count_u + 1
print("The number of uppercase characters in the string -  "  , str ,  " - is : " , count_u)
