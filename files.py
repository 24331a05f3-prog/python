try:
    srcfile=open("readfrom.txt","r")
    temp=srcfile.readline()
    print(temp)
    srcfile.seek(0)
    temp2=srcfile.readlines()
    print(temp2)
    srcfile.seek(0)
    temp3=srcfile.read()
    print(temp3)

    destfile=open("writeto.txt","w")
    destfile.write(temp3)
    destfile.writelines(temp3)
except FileNotFoundError:
    print("file doesn't exist on Disk!")
srcfile.close()
destfile.close()