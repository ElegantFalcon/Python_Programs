def vowel(str) :
    count = 0
    str1 = str.lower()
    print(str1)
    for i in str1:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count+=1
    if count == 0:
        print('No vowels found')
    else:
        print('Total vowels are :' , count)
    
st = input('Enter a string :')
vowel(st)