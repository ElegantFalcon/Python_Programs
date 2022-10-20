class Invoice() :
    def __init__(self ,part_num , part_desc , qua , price) :
        self.part_num = part_num
        self.part_desc = part_desc
        self.set_price(price)
        self.set_qua(qua)

    def set_price(self , price) :
        if (price < 0) :
            self.price = 0
            print("Price shpuld be a positive value !!")
        else :
            self.price = price 

    def set_qua(self , qua) :
        if (qua < 0) :
            self.qua = 0
            print("Quantity shpuld be a positive value !!")
        else :
            self.qua = qua

    def getInvoice(self) : 
        print("Product name : " , self.part_desc)
        print("Product price : " , self.price)
        print("Quantity : " , self.qua )
        amt = self.qua * self.price
        print("Total amount is : " , amt )
i1 = Invoice('6464','Pen', 0 , 5 )
i1.getInvoice()
