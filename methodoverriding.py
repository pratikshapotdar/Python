class person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmp(self):
        return False
class employee(person):
    def isEmp(self):
        return True
Emp = person("ravi")
print("Name: ",Emp.getName())
print("Is Employee: ",Emp.isEmp())
Emp = employee("Darshit")
print("Name: ",Emp.getName())
print("Is Employee: ",Emp.isEmp())
    