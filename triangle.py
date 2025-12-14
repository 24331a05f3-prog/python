from math import sqrt
a=int(input("enter 1st side of triangle:"))
b=int(input("enter 2nd side of triangle:"))
c=int(input("enter 3rd side of triangle:"))
s=(a+b+c)/2
print("area of the triangle is:",sqrt(s*(s-a)*(s-b)*(s-c)))
