# to avoid errrors we can use functions with default arguments
class test:
    def add(self,p=0,q=0,r=0,s=0):
        return (p+q+r+s)
t1 = test()
r1 = t1.add(10,20,30,40)
print("addition of 4 parameters is: ",r1)
r2 = t1.add(10,20,30)
print("addition of 3 parameters is: ",r2)
r3 = t1.add(10,20)
print("addition of 2 parameters is: ",r3)

