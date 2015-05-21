# -*- coding: utf-8 -*-
import sys

def main():
#    sys.path.append("F:\eclipse_workspace\import_modle\src\com\bim\FucTest.py")
    sys.path.append(r'F:\eclipse_workspace\import_modle\src\com\bim')
    moduleName = "FucTest"
    className = "CT"
    methodName = "add"
    
    module = __import__(moduleName)
    print module
    
    c = getattr(module,className)
    #CallFunction(fileName, moduleName, className, methodName, 'a')
    a = c()
    a.echo()
    print 'end'

    pass

if __name__ == '__main__':
    main();