class Profile():
    dept="IT"
    def __init__(self,name):
        self.name=name
    def sub(self,holiday):
        print(self.name)
        print ("{} is Holiday".format(holiday))


maruthu=Profile("Maruthu")
print(maruthu.name)
print(Profile.dept)
maruthu.sub("suday")

import math
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def circuference(self):
        return 2*self.radius*math.pi
    def area(self):
        return math.pi*(self.radius**2)
circ=Circle(2)
print(circ.circuference())
print(circ.area())

class playing():
    def __init__(self,name):
        self.name=name
        print ("Play Game")
    def game(self):
        print ("Do you want to play {}?".format(self.name))
# cricket=playing("cricket")
# cricket
# cricket.game()

import datetime
class city(playing):
    now=datetime.date.today()
    # def __init__(self,name):
    #     playing.__init__(self)
    #     self.name=name
    def date(self,city_name):
        print ("We Playing {} on {} at {}".format(self.name,city.now,city_name))
cricbuzz=city("Cricket")
cricbuzz.date("Chennai")
print(city.now)
class text():
    def __init__(self,name):
        self.name=name
    def open(self):
        with open(self.name,"r") as myfile:
            d=myfile.readlines()
            for i in d:
                print i

class excel():
    def __init__(self,name):
        self.name=name
    def open(self):
        with open(self.name,"r") as myfile:
            d=myfile.readlines()
            for i in d:
                print i
# with open("../game/tictoe.py","r") as myfile:
#     d=myfile.readline()
#     for i in d:
#         print i
textfile=text("../game/tictoe.py")
excel=excel("../openfile.py")
# for i in [textfile,excel]:
#     i.open()
# import os
# with open("/home/maruthu/Downloads/db.xlsx","r") as excelfile:
#     excel=excelfile.readlines()
#     for i in excel:
#         print i
# import os
# print(os.system(os.name))
def readerfun(openfile):
    openfile.open()
readerfun(excel)
readerfun(textfile)
