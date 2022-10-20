def div():
    print("-----------clear------------")
    div3 = []
    div5 =[]
    for i in range (1 , 100 ) :
        if i%3 == 0 :
           div3.append(i)
    print("The numbers divisible by 3 are : ")
    print(div3)
    for i in range (1 , 100 ) :
        if i%5 == 0 :
            div5.append(i)
    print("The numbers divisible by 5 are : ")
    print(div5)
    print("The numbers divisible by both 5 and 3 are : " , list(set(div3) & set(div5)))

div()
