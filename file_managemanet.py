import os
sample = input('enter 1 to write, 2 to read, 3 to append')
if sample == '1':
    allfile = os.listdir()
    while True:
        print([x for x in allfile if x.endswith ('.txt')])
        fname = input ('enter file name')
        if fname in allfile:
            print('file already exist')
        else:
            data=input('enter data to write')
            file=open(fname,'w')
            file.write(data)
            file.close()
            break
elif sample=='2':
    allfile=os.listdir()
    while True:
        print([x for x in allfile if x.endswith ('.txt')])
        fname=input('enter file name')
        if fname in allfile:
            file=open(fname,'r')
            print(file.read())
            break
        else:
           print('no such file exist')
elif sample=='3':
    allfile=os.listdir()
    while True:
        print([x for x in allfile if x.endswith('.txt')])
        fname=inp('enter file name')
        if fname in allfile:
            data=input('enter data to write')
            file=open(fname,'a')
            file.write(data)
            file.close()
            break
        else:
            print('no such file exist')
