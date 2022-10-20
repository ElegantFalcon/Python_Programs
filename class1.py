class Product :
    name = "pen "
    category = "stationary"
    price = 10
    
    def display_pro(self):
        print("Name : " , self.name)
        print("Category : " , self.category)
        print("Price : " , self.price)

product1 = Product()
print(product1.name)
product1.display_pro()
product2 = Product()
print("-----------------------------------")
print(product2.price)
product2.name = "pencil"
product2.display_pro()