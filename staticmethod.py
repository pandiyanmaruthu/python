class cls:
    game="cricket"
    def __init__(self,name,number):
        self.name=name
        self.number=number

mycls=cls("maruthu",11)
print(mycls.game)
print(mycls.name)
print(mycls.number)
print(cls.game)

from datetime import date
class condition:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def clsmet(cls,name,year):
        return cls(name,date.today().year-year)
    @staticmethod
    def isAdult(age):
        if age>18:
            return True
        else:
            print ("Wait for {} Years".format(18-age))
men1=condition("maruthu",25)
men2=condition("pandiyan",24)
men3=condition.clsmet("vinoth",24)
print(men1.age)
print(men2.name)
print(men3.age)
condition.isAdult(14)
