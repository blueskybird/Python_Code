f=open(r'F:\totaldata.txt','w')
a=[]
for i in range(10):
    a.append(str(i))

f.writelines(a)

f.close()
