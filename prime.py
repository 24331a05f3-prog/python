x=int(input("enter a integer:"))
isprime=0
for i in range(2,x//2+1):
    if(x%i==0):
        isprime=1
        print("the number is not prime")
        break
if(isprime==0):
    print("the number is prime")