class User_Details():
    def __init__(self,name,street,city,pincode):
        self.name=name
        self.street=street
        self.city=city
        self.pincode=pincode
    def __str__(self):
        return ("{} is living in {} it's comes under {} district".format(self.name,self.street,self.city))
    def __int__(self):
        return self.pincode
    def __del__(self):
        print "{} Deleted successfully".format(self.name)
user1=User_Details("Maruthu","West Street","Perambalur",621717)
print (user1)
print (str(user1))
print int(user1)
del user1
# print (user1)

import numpy
# print (math.sqrt(10))
print(numpy.subtract((10,24),(12,8)))

