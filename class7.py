class Department():
    def __init__(self, id, head, sub):
        self.id = id
        self.head = head
        self.sub = sub

    def disp(self):
        print("ID Number : ", self.id)
        print("Department head : ", self.head)
        print("subject : ", self.sub)

# dep1 = Department("435245" , "Dr Aswathy " , "Physics")
# dep1.disp()


class Student(Department):
    def __init__(self, name, sem, place, id, head, sub):
        self.name = name
        self.sem = sem
        self.place = place
        super().__init__(id, head, sub)

    def disp(self):
        print("Name : ", self.name)
        print("Semester : ", self.sem)
        print("Place  : ", self.place)
        super().disp()

st1 = Student("vivek" , "First sem" , "calicut", "435245" , "Dr Aswathy " , "Physics")
st1.disp()

