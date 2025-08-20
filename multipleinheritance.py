class A:
    a = 10
    def method1(self):
        print("method od A")
class B:
    b = 20
    def method2(self):
        print("method2 of B")
class C(A,B):
    c = 30
    def method3(self):
        print("method3 of C")
obj = C()
obj.method1()
obj.method2()   
obj.method3()
print("a= ", obj.a)
print("b= ", obj.b)
print("c= ", obj.c)
