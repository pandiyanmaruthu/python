class first:
    def myfun(self,name):
        print("hello"+name)
fun=first()
fun.myfun(" maruthu")

class second:
    def __init__(self,name):
        self.name=name
    def myfun(self,test):
        print(self.name+test)
fun=second("Maruthu")
fun.myfun(" Linux Welcomes")

class third:
    def __init__(self,name):
        self.name=name
    def myfun(self,act):
        self.act=self.name+act
    def inp(self):
        return self.act
out=third("maruthu")
out.myfun(" working")
print(out.inp())

class fourth:
    __hiddval=0
    def fun1(self,incr):
        self.__hiddval+=incr
        return self.__hiddval
mycls=fourth()
print(mycls.fun1(20))
print(mycls._fourth__hiddval)

class myfun():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return ("The string of a is %s and b is %s" %(self.a,self.b))
    def __repr__(self):
        return ("The repr string is a=%s and b=%s" %(self.a,self.b))
mycls=myfun("maruthu","pandiyan")
print(mycls)
print([mycls])

class firstcls(object):
    def __init__(self,name):
        self.name=name
    def empname(self):
        return self.name
    def isemp(self):
        return False
class secondcls(object):
    def __init__(self,loc):
        self.loc=loc
    def test(self):
        print (self.loc)
mycls1=firstcls("Maruthu")
print (mycls1.empname(),mycls1.isemp())
mycls12=secondcls("Pandiyan")
# print (mycls12.empname(), mycls12.isemp())
# print (mycls12.test())
print (issubclass(secondcls,firstcls))
print(issubclass(firstcls,secondcls))
print(isinstance(mycls1,secondcls))
print (isinstance(mycls12,firstcls))

# class thirdcls(firstcls,secondcls):
#     def __init__(self):
#
#         firstcls.__init__(self,name="Maruthu")
#         secondcls.__init__(self,loc="chennai")
#         print "All Drived"
#     def thirdclsfun(self):
#         print(self.test())
#     def thirdclsfun1(self):
#         print(self.empname())
# third1=firstcls("varun")
# third2=secondcls("chennai")
# myobj=thirdcls(third1,third2)
# myobj.thirdclsfun1()
#
#
# class class1:
#     def __init__(self,name):
#         self.name=name
#
#     def test(self):
#         print (self.name)
# class class2:
#     def __init__(self,city):
#         self.city=city
# fun1=class1("maruthu")
# fun2=class2("chennai")
# class outcls(class1,class2):
#     def __init__(self):
#         class1.__init__(fun1)
#         class2.__init__(fun2)
#
#     def myout(self):
#         print (self.city,self.name)
# # fun1=class1("maruthu")
# # fun2=class2("chennai")
# fun=outcls()
# fun.myout()

class par():
    def __init__(self,x):
        self.x=x
class child(par):
    def __init__(self,x,y):
        par.x=x
        self.y=y
    def mult(self):
        return self.y*par.x
out1=par(20)
y=(out1.x)
out=child(y,5)
print (out.mult())


class X(object):
    def __init__(self, a):
        self.num = a

    def doubleup(self):
        self.num *= 2


class Y(X):
    def __init__(self, a):
        X.__init__(self, a)

    def tripleup(self):
        self.num *= 3


obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)