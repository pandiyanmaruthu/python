items=[1,24,56,45,2,3,4,5,6,19,10]
for i in items:
    if  (i%2==0):
        print ("even Numbers:{}".format(i))
    elif (i%2!=0):
        print (i)
    else:
        print (i)
tup=[(1,2,3,4,5),(34,5,6,3,4),(65,4,5,6,7)]
for i,j,k,l,m in tup:
    print(i)

k={"k1":"maruthu","k2":"python","k3":"linux"}
for i,j in k.items():
    print ("key: {} value: {} ".format(i,j))

sum=0
for i in items:
    sum+=i
    print (sum)
print (sum)
print(744/24)






