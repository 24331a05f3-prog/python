x=int(input("enter how many numbers in series you want:"))

#with recursion
def fib(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fib(num-1)+fib(num-2)
print("with recursion")
for i in range(1,x+1):
    print(fib(i),end=" ")

#without recursion
fib1=0
fib2=1
print("\nwithout recusrion")
for i in range(1,x+1):
    print(fib1,end=" ")
    temp=fib1
    fib1=fib2
    fib2=temp+fib2
