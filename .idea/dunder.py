# class mydun:
#     def __init__(self,strng):
#         self.strng=strng
#     def __repr__(self):
#         return "Object:{}".format(self.strng)
#     def __add__(self,other):
#         return self.strng + other
# clssdun=mydun("Linux ")
# print(clssdun + 'world')
# l={1,2,4,5,6,7,8,8,98,4,4,4,44}
# for i in l:
#     print (i)
#
# people = {"Jay", "Idrish", "Archil"}
# vampires = {"Karan", "Arjun","Jay"}
# print(people+vampires)
# def myfun():
#     pass
#
# for i in range(1,4):
#     pass
#
#
# def yeil(x):
#     yield x
#
# for i in yeil(list(range(1,10))):
#     print i
#
# def yei():
#     i=1
#     while True:
#         yield i*i
#         i+=1
# for num in yei():
#     if num==100:
#         break
#     print num
# class myclas:
#     def __init__(self,name,area):
#         self.name=name
#         self.area=area
# cls=myclas("maruthu","perambalur")
# print(cls.name)
#
# def mul(*num):
#     num1=1
#     for i in num:
#          num1=num1*i
#     print num1
# # print(mul(12,4,4,5,6,7,7,8,8,8,432,32))
# class datab:
#     def __init__(self,**args):
#         self.args=args
#
#     num = 1
#     while num<=3:
#         print "User" + str(num) + " Details:"
#         def keyw(self,**args):
#
#
#             for i,j in self.args.iteritems():
#                 print "{}={}".format(i,j)
#         num+=1
# dat=datab(name="maruthu",city="chennai",age=23)
# dat1=datab(name="pandiyan",city="Perambalur",age=26)
# dat3=datab(name="varun",city="kanyakumari",age=26)
# dat.keyw()
# dat1.keyw()
# dat3.keyw()
def out(text):
    text=text
    def inn():
        print(text)
    inn()
if __name__ == "__main__":
    out("maruthu")

