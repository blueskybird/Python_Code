#coding=UTF-8
import sys

class TestClass:
    def sub(self,a,b):
        return a-b
    def add(self,a,b):
        return a+b
    def echo(self):
        print "test"

def main():
    sys.path.append(r'F:\eclipse_workspace\import_modle\src\com\bim')
    sys.path.append(r'F:\eclipse_workspace\import_modle\src\com\test')
    sys.path.append(r'F:\eclipse_workspace\import_modle\src\com\ls')
    print sys.path
    module = __import__('test2')
    print module
    c = getattr(module, 'Test1')
    
    a = c()
    
    a.te()
#    class_name = "TestClass" #类名
#    module_name = "beijiazai"   #模块名
##    module_name = "com.bim.beijiazai"   #模块名
#    method = "echo"          #方法名
#
#    module = __import__(module_name) # import module
#    print "#module:",module
##    c = getattr(module,class_name)
#    c = getattr(module, 'TestClass')  
#    print "#c:",c
#    obj = c() # new class
#    print "#obj:",obj
#    print(obj)
#    obj.echo()
#    mtd = getattr(obj,method)
#    print "#mtd:",mtd
#    mtd() # call def
#    
#    mtd_add = getattr(obj,"add")
#    t=mtd_add(1,2)
#    print "#t:",t
#
#    mtd_sub = getattr(obj,"sub")
#    print mtd_sub(2,1)


if __name__ == '__main__':
   main()

