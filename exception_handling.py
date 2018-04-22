try:
    num=a+10
except (TypeError, NameError) as e:
    print "Error"
finally:
    print "Always i run"

try:
    with open("clear_output1.py","r") as myfile:
        d=myfile.readlines()
        for i in d:
            print i
except IOError, TypeError:
    print "File Not found"
else:
    print ("File Found")

while True:
    try:
        num=input("Please enter Number: ")
    except:
        print ("It's not a number")
        continue
    else:
        print ("Success {}".format(num))
        break
    finally:
        print ("I always run!!")


