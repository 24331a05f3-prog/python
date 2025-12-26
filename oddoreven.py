x=int(input("enter your range:"))
counte=0
counto=0
for i in range(1,x+1):
    if(i%2==0):
        counte+=1
    else:
        counto+=1
print("the number of odd and even numbers respectively:",counto,'and',counte)