class student:
    def __init__(self,a=18,g="male",d="cs"):
        self.age = a
        self.gender = g
        self.department = d
    def show_values(self):
        print("age: ",self.age)
        print("gender: ",self.gender)
        print("department: ",self.department)
s1 = student()
s2 = student(19,"female","IT")
print("Initialised values of 1st student")
s1.show_values()
print("Initialised values of 2nd student")
s2.show_values()
