name="Maruthu Pandiyan"
mylist=[]
for i in name:
    mylist.append(i)
print mylist

list=[45,323,6,3.32]
mylist1=[((9/5)*i+32) for i in list ]
print mylist1

ran=range(1,5)
ran1=[i if i%2==0 else "odd" for i in ran]
print ran1
ran2=range(1,3)
ran3=[i*j for i in ran for j in ran2 ]
print ran3
test=name.split()
print test

