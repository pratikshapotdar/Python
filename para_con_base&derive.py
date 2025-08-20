# parameterized constructor in base class and derive class
class person:
    def __init__(self,name,id_no):
        self.name = name
        self.id_no = id_no
class emp(person):
    def __init__(self,name,id_no,salary,post):
        person.__init__(self, name, id_no)
        self.salary = salary
        self.post = post
    def display__emp__details(self):
        print("Name: ",self.name)
        print("ID No.: ",self.id_no)
        print("salary: ",self.salary)
        print("Post: ",self.post)
e1 = emp("Darshit",45520,6500,"manager")
e1.display__emp__details()


        