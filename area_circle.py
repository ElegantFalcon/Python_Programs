def area(r=None, l=None, b=None):
    if r != None :
        area = 3.14*r*r
        print("The area of circle is: " , area , "units")
    elif l!= None and b!= None :
        ar_rec = l*b
        print("The area of rectangle is: " , ar_rec , "units")

# radius = int(input("Enter radius of the circle : "))
area(l = 2, b = 3)
area(1)