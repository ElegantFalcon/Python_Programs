# str1 = []
# str1 = input("Enter a string : ")
 
# # printing original list
# #print("The original list : " + str(str1))
 
# # Convert String list to ascii values
# # using loop + ord()
# res = []
# for ele in str1:
#     res.extend(ord(num) for num in ele)
#  # printing result
# print("The ascii list is : " + str(res))
# print("------------------------------------------------------------------------------------------")
# #print(res[0])

# #condition to check for uppercase and length
# count_upper = 0
# if len(str1) > 7 :
#     for i in range(65 , 90 ) :
#         if res[0] == i :
#             count_upper = count_upper + 1
#         else :
#             count_upper = 0
# else :
#     print("Weak password !!!")

# #condition to check for special character
# spl_count = 0
# if count_upper == 1:
#     for i in str1:
#             if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i =='&' or i == '*':
#                 spl_count += 1

# #condition to check for two numbers
# digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# digits_count = 0
# if count_upper == 1 and spl_count >= 1 :
#     for s in str1:
#        if s in digit_list:
#         digits_count += 1

# if count_upper == 1  and spl_count >= 1 and digits_count >= 2 :
#     print("Strong Password!!!")


str1 = input("Enter a string : ")
upper = 0
length = len(str1)
spl_count = 0
digits_count = 0


if(str1[0].isupper()):
    upper += 1
    
for i in str1:
    if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i =='&' or i == '*':
        spl_count += 1

digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for s in str1:
    if s in digit_list:
        digits_count += 1

if upper == 1  and spl_count >= 1 and digits_count >= 2  and length >= 8 :
    print("Strong Password!!!")
else:
    print("Weak Password!!!")







