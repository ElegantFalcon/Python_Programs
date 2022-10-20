class Doctor():
    def __init__(self,name , exp , qual , place) :
        self.name = name 
        self.exp = exp
        self.qual = qual
        self.place = place 


    def disp(self):
        print("Name :" , self.name)     
        print("Qualification : " , self.qual)   
        print("Years of experience : " , self.exp)
        print("Place : " , self.place)

    def operate(self):
        print("Number of succesful surgeries is : 90")

doctor1 = Doctor("Ajay" , 45 , "MBBS,MD" , "Calicut")
doctor1.disp()
doctor1.operate()


        
    