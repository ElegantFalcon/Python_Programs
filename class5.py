class Account() :
    def __init__(self ,name , amount) :
        self.name = name
        self.set_amount(amount)

    def det(self):
        print("Name : " , self.name)
        print("Amount : " , self.__amount)

    def set_amount(self , amount) :
        if (amount < 0) :
            self.__amount = 0
        else :
            self.__amount = amount 

    def get_amount(self):
        return self.__amount


# acc2 = Account("Vijay" , 65524)
# print(acc2.get_amount())




        