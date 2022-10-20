

price =[]
item_count = int(input("Enter total number of items : "))
i=0
while i<=item_count-1 :
    num = int(input('Enter  price : '))
    price.append(num)
    i+=1
print(price)

amount = sum(price)
print ("Total amount : " , amount)
discount = 0
net_amount=0
if amount <= 2000:
    print("No Discount !!!")
elif amount > 2000 and amount <= 5000 :
    print("You have 12% discount")
    discount = (12/100)*amount 
    net_amount = amount - discount
    print ("Discount : ", discount)
    print ("Amount to be paid : " , net_amount)
elif amount > 5000 and amount <= 10000 :
    print("You have 18% discount")
    discount = (18/100)*amount 
    net_amount = amount - discount
    print ("Discount : ", discount)
    print ("Amount to be paid : " , net_amount)
elif amount > 10000 :
    print("You have 25% discount")
    discount = (25/100)*amount 
    net_amount = amount - discount
    print ("Discount : ", discount)
    print ("Amount to be paid : " , net_amount)





