class A:
    def __init__(self):
        print("constructor of class A")
    def __del__(self):
        print("destructor of class A")
class B(A):
    def __init__(self):
        print("constructor of class B")
    def __del__(self):
        print("destructor of class B")
obj=B()