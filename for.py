n=int(input("Enter value of n: "))
sum = 0
for i in range(1, n + 1):
    sum = sum+i
    i = i + 1
print("Sum of first n natural numbers is: ", sum)