class Area():
    def area(self, r = None, l = None, b = None):
        if r != None:
            a_c = 3.14 *r* r 
            print("Area of circle is : " , a_c)
        else:
            a_r = l *b
            print("Area of rectangle is : " , a_r)
            


ar1 = Area()
ar1.area(l = 10 , b = 10)
        