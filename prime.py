x=int(input("enter a integer:"))
#without recursion
isprime=0
for i in range(2,x//2+1):
    if(x%i==0):
        isprime=1
        print("the number is not prime(without recursion)")
        break
if(isprime==0):
    print("the number is prime (without recursion)")

#with recursion
def prime(x):
    global i
    if(i<=x//2):
        if(x%i==0):
            return 1
        else:
            i=i+1
            return prime(x)
    else:
        return 0
i=2
y=prime(x)
if(y==1):
    print(x,"is not a prime number (with recursion)")
else:
    print(x,"is a prime number (with recursion)")
