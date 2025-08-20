# use of super to access parent class methods
class A:
    def sayHello(self):
        print("Hello from A")
class B(A):
    def sayHello(self):
        print("Hello from B")
    def greet(self):
        super(B,self).sayHello()
        self.sayHello()
b1 = B()
b1.greet()