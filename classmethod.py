class myclass():
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def addrs(self):
        return ("Name:" +self.name + "City: "+self.city )
    @classmethod
    def myclsmethod(cls,val):
        return cls(val,val)

out=myclass.myclsmethod("chennai ")
print(out.addrs())

class mycls1():
    def __init__(self,fruites):
        self.fruites=fruites
    @staticmethod
    def mystat(fruites):
        if fruites=="apple":
            return False
        else:

            return True
list1=["banana","lemon","orange","apple"]
if any(mycls1.mystat(i) for i in list1):
    print (True)
else:
    print (False)
class propertycls():
    def __init__(self,val):
        self.val=val
    @property
    def propermet(self):
        return True
out=propertycls(["maruthu","chennai"])
print(out.propermet)
out.propermet=False
print(out.propermet)

class setclass():
    def __init__(self,val):
        self.val=val
        self._methret=False
    @property
    def methretr(self):
        return self._methret
    @methretr.setter
    def mehtretr(self,val):
        if val:
            passwd=input("Please Enter Your Passwored:")
            if "Maruthu"==passwd:
                self.methretr=True
            else:
                raise ValueError("Enter Correct Passwd")
myout=setclass(["Maruthu","Chennai"])
print(setclass.methretr)


class supcls(object):
    def __init__(self,name):
        self.name=name
    def empName(self):
        return self.name
    def isEmp(self):
        return True
class subcls(supcls):
    def __init__(self,name,empid):
        super(subcls,self).__init__(name)
        self.empid=empid
    def isEmp(self):
        return False
    def empiddef(self):
        return self.empid
mycls=subcls("maruthu",345)
print(mycls.isEmp(),mycls.empiddef(),mycls.name)


def game():
    input1=input(":").split
    val0=input1[0]
    if val0 in val_dict:
        verb=val_dict[val0]
    else:
        print("Unknown Val {}".format(val0))
        return
    def say(noun):
        return ("You Said{}".format(noun))
    val_dict={"say":say}