#Python Lambda Functions are anonymous function means that the function is without a name.
#  As we already know that the def keyword is used to define a normal function in Python.
# Similarly, the lambda keyword is used to define an anonymous function in Python. 

x =lambda x:x+10
print(x(4))


cal = lambda x,y,z : x+y*z
print(cal(2,3,4))


print((lambda a,b,c : a+b+c)(1,2,23))