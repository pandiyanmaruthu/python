# import numpy as np
# mymatrx=np.zeros((5,5))
# print ("Zero Matrix")
# print(mymatrx)
# print ("5x5 Matrix: ")
# mymatrx+=np.arange(5)
# print (mymatrx)
# print (mymatrx[4][1])
# def myfun(nums):
#     mynum=[0,0,7,'x']
#     for i in nums:
#         if i==mynum[0]:
#             mynum.pop(0)
#     if len(mynum)==1:
#         return True
#     else:
#         return False
# print(myfun([1,1,1,2,4,4,0,0,1,2,4,5,0]))

def primenum(num):
    if num<2:
        return False
    prime=[2]
    a=3
    while a<num:
        for b in range(3,a,2):
            if a%b==0:
                break
        else:
            prime.append(a)
        a=a+2
    print (prime)
    print (len(prime))
if __name__=="__main__":
    pass
primenum(24)
numb=12
def sample():
    # global numb
    # numb="Learning Python"
    print numb
print numb
sample()
print numb

# name="Maruthu Pandi"
# newname=name.replace("Pandi","Pandiyan")
# print newname
# names=["maruthu","pandiyan"]
# print (" ".join(names))
# print(name[::-1])
# print (name.split("a"))

name="Maruthu Pandiyan"
def myfun(name):
    print (name)
    name="vijay"
    print ("local name is {}:".format(name))
    return name
name=(myfun(name))
print (name)
