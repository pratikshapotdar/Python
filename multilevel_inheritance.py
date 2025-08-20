class A:
    a = 10
    def method1(self):
        print("Method of class A")
class B(A):
    b = 20
    def method2(self):
        print("Method of class B")
class C(B):
    c = 30
    def method3(self):
        print("Method of class C")
obj = C()
obj.method1()
obj.method2()
obj.method3()
print("a =", obj.a)
print("b =", obj.b)
print("c =", obj.c)
        