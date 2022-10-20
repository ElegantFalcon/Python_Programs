def sp_char(str) :
    count = 0
    str1 = str.lower()
    print(str1)
    for i in str1:
        if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i =='&' or i == '*':
            count+=1
    if count == 0:
        print('No special characters found')
    else:
        print('Total special characters  are :' , count)
    
st = input('Enter a string :')
sp_char(st)