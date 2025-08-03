def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
print("Enter value of n: ")
n = int(input())
res = fact(n)
print("Factorial is: ", res)