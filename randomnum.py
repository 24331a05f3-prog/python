import random
try:
    dest=open("random.txt","w")
    for i in range(20):
        dest.writelines(str(random.randint(1,100))+",")
except FileNotFoundError:
    print("file doesnt exist in your list")