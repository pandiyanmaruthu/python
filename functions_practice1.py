def myfunc(name):
    print name[2]
    return name[0].upper() + name[1:3] + name[3:9] + name[9].upper() + name[9:]
print(myfunc("maruthu pandiyan"))

def func(cps):
    return cps[:3].capitalize() + cps[3:].capitalize()
print(func("pythonlinux"))

name=["hello","maruthu","welcome"]
print(len(name))
print " ".join(name)
def rev(strn):
    out=[""]
    new_strn=strn.split()
    print new_strn
    lent=len(new_strn)-1
    print lent
    while 0<=lent:
        out.append(new_strn[lent])
        lent-=1
    return " ".join(out)
print(rev("linux windows mac"))
print(rev("Hello welcomes to tamilnadu"))
setc=["hello","welcome"]
out=setc[::-1]
print out
print (abs(100-90))


def hasmaruthu():
    lst=["maruthu","maruthu","pandiyan","vnpuram","vnpuram"]
    for i in range(len(lst)-1):
        if lst[i]=="vnpuram" and lst[i+1] == "vnpuram":
            return True
    return False
print(hasmaruthu())

def fun(name):
    str=""
    for i in name:
        str+=i*3
    return str
print(fun("paunkumar"))
# print(sum(1,2,3))

def calc(a,b,c):
    if (a+b+c)>=21 and (a==11 or b==11 or c==11):
        return "BUST"
    elif (a+b+c)<=21:
        return (a+b+c)
    elif (a+b+c)>=21:
        return (a+b+c)
print(calc(12,3,11))
lit=[1,2,3,4,5]
print(lit.index(5))


def retu(num):
    sm=0
    ret=True
    # if 6 in num and 9 in num:
    #     ind1=num.index(6)
    # #     ind2=num.index(9)
    #     for i in num:
    #         if num==6:
    #             while not num==9:
    #                continue
    #         else:
    #             sm+=num
    #     return sm
    # else:
    #     return sum(num)
    for i in num:
        while ret:
            if i!=6:
                sm+=i
                break
            else:
                ret=False
            return ret
        while not ret:
            if i!=9:
                ret=True
            else:
                sm+=i
            return ret

    return sm
print(retu(1,2,545))




# print(retu(1,2,4,5,5))
#
#
#
#
#
#                 continue
#             else:
#                 sum+=i
#
#
# print retu(1,2,3,4,4,5,5,5,9)

