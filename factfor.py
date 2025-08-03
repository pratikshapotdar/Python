n = int(input("Enter value of n: "))
fact = 1
for i in range(1, n + 1):
    fact *= i   
    n = n - 1
print("Factorial is: ", fact)