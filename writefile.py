
with open("/tmp/test10.txt") as file:
    print(file.read())
print(os.getcwd())
with open("/tmp/test10.txt","w+") as file:
    lines="""Hi this is linux oriented python program,
    it's interepted using pycharm, and this one is easy
    to configure all the codes."""
    write=(file.write(lines))
    print(file.readlines())
with open("/tmp/test10.txt","r") as file:
  myfile=file.readlines()
  for i in myfile:
      print (i)
with open("/tmp/test10.txt") as file:
    print(file.read())
    print("")
    print(file.read())
    print(file.seek(0))
    print("")
    print(file.read())
num=10**2
print(num)
list=[1,2,34]
list1=list*4
print(sorted(list1))
