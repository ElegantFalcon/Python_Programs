def tri(a , b, c) :
    if a == b and b==c and c == a :
        print("The traingle with sides " , a , "," , b , "," ,c ," is an Equilateral Triangle")
    elif a == b or b==c or c == a :
        print("The traingle with sides " , a , "," , b , "," ,c ," ia an Isoceles Triangle")
    else :
        print("The traingle with sides " , a , "," , b , "," ,c ," is a Scalene Triangle")

s1 = int(input("Enter the length of first side : "))
s2 = int(input("Enter the length of second side : "))
s3 = int(input("Enter the length of third side : "))
tri(s1 , s2 , s3 )