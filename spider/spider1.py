def foo():
    return True

def bar():
    'bar() dose not do much'
    return True

foo.__doc__='foo() does not do much'

foo.tester='''
if foo():
    print 'PASSED'
else:
    print 'FAILED'
'''

for eachAttr in dir():
    print type(eachAttr),eval(eachAttr),type(foo)
    print isinstance(eval(eachAttr),type(foo))
