num=int(input("enter a positive number:"))
#with recursion
def fact(x):
    if x==0 or x==1:
        return 1;
    else:
        return x*fact(x-1)
print("with recursion",fact(num))

#without recursion
fact=1
for i in range(1,num+1):
    fact=fact*i
print("without recusrion",fact)
