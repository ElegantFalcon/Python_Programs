class Employee():
    def __init__(self,name , join_date , email, comp_name , place) :
        self.__name = name 
        self.join_date = join_date
        self.email = email 
        self.comp_name = comp_name
        self.place = place 


    def disp(self):
        print("Name :" , self.__name)     
        print("Company name : " , self.comp_name)   
        print("Joining date: " , self.join_date)
        print("Email id : " , self.email)
        print("Place : " , self.place)

    def release_amt(self , amt):
        print("The release amount of the employee is : " , amt)




emp1 = Employee("Ajay" , "05 - 08 -2022" , "ajay.code@gmail.com" , "acemero"  ,"Calicut")
emp1.disp()
emp1.release_amt("25868132")


        
    