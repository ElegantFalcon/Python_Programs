#static polymorphism --- overriding
class Employees():
    def release(self) :
        print("release 30000")

class Manager(Employees):
    def release(self) :
        print("Release 300000")

m1 =  Manager()
m1.release()

e1 = Employees()
e1.release()

