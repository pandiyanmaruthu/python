ind=[1,2,3,4,5,5]
try:
    # raise ValueError
    for i in range(5):
        print ind[i]

except (NameError,IndexError,ValueError):
    print "Value Error Occured."
    raise
else:
    print ind

def myint(a,b):
    if a==20 or b==20 or a+b==20:
        return True
    else:
        return False
print(myint(20,200))
