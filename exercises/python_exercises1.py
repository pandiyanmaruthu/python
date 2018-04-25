## File exists check

from __future__ import print_function
def exercise():
    import os.path
    print (os.path.isfile("../game/blackjack1.py"))
    print (os.path.isdir("../game"))

    ##Get Platform
    import platform
    print (platform.architecture())

    ##Get OS name,Platform and Release
    print (platform.system())
    print (platform.platform())
    print (platform.release())

    ## Get Site Packages
    import site
    print (site.getsitepackages())

    ##Call External command in python
    from subprocess import call
    print (call(["ping","-c1","192.168.175.56"]))
    print (call(["ps","aux"]))
    print (call(["systemctl","status","smb"]))
    print (call(["df","-HT"]))
    ##Print Current Working Directory and current working file
    print (call([("pwd")]))
    import os
    print (os.getcwd())
    import sys
    name=(sys.argv[0])
    print (name)
    print (call(["basename",name,".py"]))

    ###Get output from dict

    user_dict_value={122:"maruthu",101:"pandiyan",111:"Linux"}
    def myfun(userinput):
        return "%s is user input value" %user_dict_value.get(userinput,"Myvalue")
    print (myfun(101))
    print (myfun(1213))

    ### namedtuple alternate for class
    from collections import namedtuple
    project=namedtuple("kjk","name,duration,worth")
    python=project("python",1,12000)
    print (python.name)
    print (python.duration)
    print(python.worth)
    php=project("php",2,10000)
    print (php.name)
    print (php.duration)
    comp_dict_value={0:"shutdown",6:"Restart"}
    output_dict_value=dict(user_dict_value,**comp_dict_value)
    print (output_dict_value)

    ### Print Number of cpus
    import multiprocessing
    call(["nproc"])
    print (multiprocessing.cpu_count())
    n="32134232"
    print (float(n))
    print (int(n))
    ## Try to change directory and list files
    call(["cd","/tmp","&&","ls","-lh"])
    os.chdir("/tmp")
    print (os.getcwd())
    # call(["ls","-lh"])
    ## Listing files in directory

    from os import listdir
    from os.path import isfile,join
    varfiles=[p for p in listdir("/tmp") if isfile(join("/tmp",p))]
    print (varfiles)
    # for i in range(1,10):
    #     print ("*",end =" ")

# exercise()
### Check function processing time using profiling
import cProfile
cProfile.run("exercise()")

## Print Error, it will gives Red color output

import sys

def eprint(*args,**kwargs):
    print(*args,file=sys.stderr)

eprint("abc", "efg", "xyz", sep="--")

### Print Environment variables

import os
print ("*------------------------*")
print (os.environ)
print (os.environ['HOME'])
###print (os.environ)
## Get current Username
import getpass
print (getpass.getuser())
##Get hostname and ip addreess
import socket
print (socket.gethostname())
print (socket.gethostbyname(socket.gethostname()))
### Time to calculate sum
import time
def myclac(n):
    start_time=time.time()
    s=0
    for i in range(1,n+1):
        s+=i
    end_time=time.time()
    time_diff=end_time-start_time
    return s,time_diff
n=20
print ("Sum between 1 to",n,"and time taken is: ",myclac(n))
print ((20*(20+1))/2)




print ("test branch commit")

