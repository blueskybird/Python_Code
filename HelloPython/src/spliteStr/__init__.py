
f=open(r'C:\Users\Administrator\Desktop\11111.txt','r')

line=f.readline()

f.close()

listNum=line.split(' ')

i=0
for j in listNum:
    if j=='':
        del listNum[i]
    i+=1

sumNum=0
for j in listNum:
    sumNum+=int(j)
print sumNum