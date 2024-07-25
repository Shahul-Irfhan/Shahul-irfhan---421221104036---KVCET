import os   #library for text operations
print("enter 1 to write, 2 to read, 3 to append")
action=int(input(""))
if action==1:
    fnw=input("enter file name:")
    cont=input("enter file content")
    file=open(fnw,'w')
    file.write(cont)
    file.close()
elif action==2:
    a=os.listdir()
    for i in a:
        if i.endswith(".txt"):
            print (i)
    fnr=input("choose and enter the file")
    file=open(fnr,'r')
    file.seek(0)
    print(file.read())
    file.close()
elif action==3:
    a=os.listdir()
    for i in a:
        if i.endswith(".txt"):
            print (i)
    fna=input("choose and enter the file to append:")
    fna_cont=input("enter content to append:")
    file=open(fna,'a+')
    file.write(fna_cont)
    file.seek(0)
    print(file.read())
    file.close()
else:
    print("enter valid operation number")
