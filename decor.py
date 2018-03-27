# def myfun(fun):
#     def test():
#         print "####################"
#         fun()
#         print "####################"
#     return test
# def print_fun():
#     print "Linux"
# myfun(print_fun())
# def myfunc(x):
#     return x**3
# myfn=myfunc
# print(myfn(10))
# print(myfunc(20))
# del myfn
# # print(myfn(12))
# print(myfunc(12))
# def out():
#     def ins():
#         print "Linux"
#     print "Python"
#     ins()
# out()
#
# def ferion(t):
#     def temp2fer(x):
#         return 9 * x/5 +32
#     print "Temprature to ferionheat for {}:".format(t)
#     result=temp2fer(t)
#     return result
# print(ferion(59))
# def a():
#     print "linux"
#     print "python"
# def b(func):
#     print ("Windows")
#     print ("IIS")
#     print(func.__name__)
#     func()
# (b(a))
#
#
# import math
# def myfunc(func):
#     res=0
#     for i in [1,2,3,4,5,6,7,8,8,9,90,0,0,0,8,6,75,65]:
#         res+=func(i)
#     return res
# print(myfunc(math.cos))
# print (myfunc(math.sin))

# def myfunc(func):
#     def fun(x):
#         print ("The function name " + func.__name__)
#         func(x)
#         print ("The function name " + func.__name__)
#     return fun
# def foo(x):
#     print ("The foo output is {}".format(x))
#
# foo(20)
#
# foo=myfunc(foo)
# foo(25)
def mydec(func):
    def mysubdec(x):
        print ("Before calling fun "+func.__name__)
        func(x)
        print ("After Calling Fun "+func.__name__)
    return mysubdec
@mydec
def foo(x):
    print ("Hi,we are in {}".format(x))
foo("Linux")