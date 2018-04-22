# num=[1,2,3,4,5,6]
# print(num.index(6))
# def indx(num):
#     myindex=num.index(3)
#     nextindex=myindex+1
#     if num[nextindex]==3:
#         return True
#     else:
#         return False
# print (indx([1,3,4,53,3,6]))
def paper_doll(text):
    mytext=list(text)
    lent=len(mytext)
    output=''
    for i in range(lent):
        output+=mytext[i]*3
    return output
print(paper_doll("Maruthu Pandiyan"))
a=12
b=12
c=[]
c.append(a)
c.append(b)

print(sum([1,2,4]))
print(sum(c))
num=[1,2,3,4,5]
def myfun(num1):
    # mynum=num1.index(6)
    # nexnum=num1.index(9)
    # nexnum1=nexnum+1
    if 6 in num1 and 9 in num1:
        mynum = num1.index(6)
        print (mynum)
        nexnum = num1.index(9)
        print(nexnum)
        nexnum1 = nexnum + 1
        return sum(num1[:mynum])+sum(num1[nexnum1:])
    else:
        return sum(num1)
print(myfun([1,2,3,3,4,5,5,6,121,2,123,9,413,9]))





