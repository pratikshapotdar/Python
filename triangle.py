s1 = int(input("Enter a side of triangle:"))
s2 = int(input("Enter a side of triangle:"))
s3 = int(input("Enter a side of triangle:"))
if s1==s2 and s2==s3:
    print("triangle is equilateral")
elif s1==s2 or s2==s3 or s1==s3:
    print("triangle is isocelese")
else:
    print("triangle is scalere")