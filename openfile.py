# file1=open("obj2.py","r+")
# file1.write("Hello This is the firstline")
# print(file1.read())
# file1.close()
# import filecmp
# print(filecmp.cmp("gmail.py","gmail.py"))
with open("gmail.py") as file1:
    with open("mail.py") as file2:
        same=set(file1).intersection(file2)
same.discard("\n")
with open("newoutput","w") as out:
    for i in same:
        out.write(i)

with open("newoutput") as myfile:
    print(myfile.read())