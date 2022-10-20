class Data():
    def __init__(self , name , qualification , exp ):
        self.name = name 
        self.qualification = qualification
        self.exp = exp

    def disp(self):
        print("Name :" , self.name)     
        print("Qualification : " , self.qualification)   
        print("Years of experience : " , self.exp)


data1 = Data("ajay" , "MBBS" , 5)
data1.disp()

data2 = Data("vivek" , "MBBS, MD" , 10)
data2.disp()




