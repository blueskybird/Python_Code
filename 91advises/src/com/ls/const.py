# -*- coding: utf-8 -*-

class _const:
    class ConstError(TypeError):pass
    class ConstCaseError(ConstError):pass
    
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstCaseError,"Can't change const.%s" % name
        if not name.isupper():
            raise self.ConstCaseError,"const name '%s' is not all uppercase" %name
        self.__dict__[name]=value
        
        
import sys
sys.modules[__name__]=_const()


#可以在这个地方定义，也可以集中在一个文件中定义，比如集中在constant.py文件中定义常量
import const
const.MY_CONSTANT = 1
const.USERNAME = 'LISHUAI'
const.PASSWORD = '123456'