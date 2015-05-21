# class myDecorator(object):
#
#     def __init__(self, fn):
#         print "inside myDecorator.__init__()"
#         self.fn = fn
#         print 'init '
#
#     def __call__(self):
#         self.fn()
#         print "inside myDecorator.__call__()"
#
# @myDecorator
# def aFunction():
#     print "inside aFunction()"
#
# print "Finished decorating aFunction()"
#
# aFunction()

def decorate_A(function):
    def wrap_function(*args, **kwargs):
        kwargs['str'] = 'Hello!'
        return function(*args, **kwargs)
    return wrap_function

@decorate_A
def print_message_A(*args, **kwargs):
    print(kwargs['str'])

print_message_A()