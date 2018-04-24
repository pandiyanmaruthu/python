## File exists check
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
