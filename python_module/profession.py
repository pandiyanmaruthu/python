import inspect
print ("This is professional method")
print (__name__)
def func():
    print "Hello fuction returns {}".format(inspect.stack()[0][3])
if __name__ =="__main__":
    print ("This function is directly called")
else:
    print ("This function is imported")