a=[0]*10
tmp=[]
for i in range(len(a)):
    tmp.append(str(a[i])+',')
f=open(r'/home/lsh/Desktop/listtotxt.txt','w')
f.writelines(tmp)
f.close()
fr=open(r'/home/lsh/Desktop/listtotxt.txt','r')
l=fr.readline()
fr.close()
print type(l[0])
