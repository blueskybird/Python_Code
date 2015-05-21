

def meansandclass():
    means=[]
    classnum=[]
    f=open(r'C:\Users\Administrator\Desktop\totalData.txt','r')
    line=f.readline().strip()
    while line:
        c=[]
        spline=line.split("	")
        for i in range(len(spline)):
            if i==len(spline)-1:
                classnum.append(float(spline[i]))
            else:
                c.append(float(spline[i]))
        means.append(c)
        line=f.readline().strip()

    return means,classnum
