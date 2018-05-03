# ## File exists check
#
# from __future__ import print_function
# def exercise():
#     import os.path
#     print (os.path.isfile("../game/blackjack1.py"))
#     print (os.path.isdir("../game"))
#
#     ##Get Platform
#     import platform
#     print (platform.architecture())
#
#     ##Get OS name,Platform and Release
#     print (platform.system())
#     print (platform.platform())
#     print (platform.release())
#
#     ## Get Site Packages
#     import site
#     print (site.getsitepackages())
#
#     ##Call External command in python
#     from subprocess import call
#     print (call(["ping","-c1","192.168.175.56"]))
#     print (call(["ps","aux"]))
#     print (call(["systemctl","status","smb"]))
#     print (call(["df","-HT"]))
#     ##Print Current Working Directory and current working file
#     print (call([("pwd")]))
#     import os
#     print (os.getcwd())
#     import sys
#     name=(sys.argv[0])
#     print (name)
#     print (call(["basename",name,".py"]))
#
#     ###Get output from dict
#
#     user_dict_value={122:"maruthu",101:"pandiyan",111:"Linux"}
#     def myfun(userinput):
#         return "%s is user input value" %user_dict_value.get(userinput,"Myvalue")
#     print (myfun(101))
#     print (myfun(1213))
#
#     ### namedtuple alternate for class
#     from collections import namedtuple
#     project=namedtuple("kjk","name,duration,worth")
#     python=project("python",1,12000)
#     print (python.name)
#     print (python.duration)
#     print(python.worth)
#     php=project("php",2,10000)
#     print (php.name)
#     print (php.duration)
#     comp_dict_value={0:"shutdown",6:"Restart"}
#     output_dict_value=dict(user_dict_value,**comp_dict_value)
#     print (output_dict_value)
#
#     ### Print Number of cpus
#     import multiprocessing
#     call(["nproc"])
#     print (multiprocessing.cpu_count())
#     n="32134232"
#     print (float(n))
#     print (int(n))
#     ## Try to change directory and list files
#     call(["cd","/tmp","&&","ls","-lh"])
#     os.chdir("/tmp")
#     print (os.getcwd())
#     # call(["ls","-lh"])
#     ## Listing files in directory
#
#     from os import listdir
#     from os.path import isfile,join
#     varfiles=[p for p in listdir("/tmp") if isfile(join("/tmp",p))]
#     print (varfiles)
#     # for i in range(1,10):
#     #     print ("*",end =" ")
#
# # exercise()
# ### Check function processing time using profiling
# import cProfile
# cProfile.run("exercise()")
#
# ## Print Error, it will gives Red color output
#
# import sys
#
# def eprint(*args,**kwargs):
#     print(*args,file=sys.stderr)
#
# eprint("abc", "efg", "xyz", sep="--")
#
# ### Print Environment variables
#
# import os
# print ("*------------------------*")
# print (os.environ)
# print (os.environ['HOME'])
# ###print (os.environ)
# ## Get current Username
# import getpass
# print (getpass.getuser())
# ##Get hostname and ip addreess
# import socket
# print (socket.gethostname())
# print (socket.gethostbyname(socket.gethostname()))
# ### Time to calculate sum
# import time
# def myclac(n):
#     start_time=time.time()
#     s=0
#     for i in range(1,n+1):
#         s+=i
#     end_time=time.time()
#     time_diff=end_time-start_time
#     return s,time_diff
# n=20
# print ("Sum between 1 to",n,"and time taken is: ",myclac(n))
# print ((20*(20+1))/2)
# import os,time
# def filepath(filename):
#     return os.path.abspath(filename)
# print ("The file absolute path is",filepath("kdakf"))
#
# def filedetails(filename):
#     print ("File created on %s"%time.ctime(os.path.getctime(filename)))
#     print ("File last modified on %s"%time.ctime(os.path.getmtime(filename)))
#
# filedetails("../game/blackjack_object.py")
# print (time.ctime(time.time()))
#
# def BMI():
#     height=float(input("Input your height in meters: "))
#     weight=int(input("Input your weight in kg: "))
#     print ("Your BMI is: ",round(weight/(height**2),2))
# BMI()
# import sys
# print ("System Copy-Right is: ", sys.copyright)
# print ("System Memory model is:",sys.byteorder)
#
# print (sys.builtin_module_names)
# print ("Size of file is : ",round(os.path.getsize("../game/blackjack_object.py")/1024,2))
# import datetime
#
# print (datetime.datetime.now())
#
# import socket
# print (socket.gethostname())
# import subprocess
# # file and directory listing
# returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
# print("dir command to list file and directory")
# print(returned_text)
# import os
# print (os.path.splitext("maruth.txt"))
# import os.path
# def file_check(file):
#     print('File        :', file)
#     print('Absolute    :', os.path.isabs(file))
#     print('Is File?    :', os.path.isfile(file))
#     print('Is Dir?     :', os.path.isdir(file))
#     print('Is Link?    :', os.path.islink(file))
#     print('Exists?     :', os.path.exists(file))
#     print('Link Exists?:', os.path.lexists(file))
#
# file_check("/etc/rmt")
# num=list(filter(lambda x: x%15==0,[15,13,42,45,60,90]))
# print (num)
#
# import glob
# l=(glob.glob("*.*"))
# for i in l:
#     print (i)
# from functools import reduce
# list=[1,2,43]
# print (reduce((lambda x,y:x*y),list))
#
# str1="Maruthu Pandiyan"
# str2="Maruthu Pandiya"
# print ("Memory Location {}".format(hex(id(str1))))
# print ("Memory Location {}".format(hex(id(str2))))
# l=[20,23,21]
# x=(bytearray(l))
# for i in x:
#     print (i)
# import matplotlib.pyplot as plt
# plt.figure(figsize=(5,5))
# label=["Python","Git","Linux","Automation","Scripting"]
# value=[40,80,90,34,75]
# explode=[0,0,0.05,0,0]
# colors=["g","b","c","w","r"]
# plt.pie(value,labels=label,autopct="%.1f%%",explode=explode,colors=colors)
# plt.show()

# plt.figure(figsize=(10,10))
# names=["Python","Git","Linux","Automation"]
# value=[10,2,42,14]
# position=[0,1,2,3]
#
# plt.bar(position,value,width=0.5,color="r")
# plt.xticks(position,names)
# plt.show()
# def mydecor(decfun):
#     print ("Hello Python Decorator")
#     def subfun():
#         decfun()
#         print ("function from subfun of mydecor")
#     return subfun()
#
#
# @mydecor
# def func():
#     print ("This is python Decorator function example1")
#
# func
#
# def normal(n):
#     mylist=[]
#     for i in range(n):
#         mylist.append(i**3)
#     return mylist
# for i in normal(10):
#     print (i)
#
# print ()
# print ()
# def gen(n):
#     for i in range(n):
#         yield i**3
# for i in gen(10):
#     print (i)
# mygen=gen(10)
# print (mygen)
# print (next(mygen))
# print (next(mygen))
# print (next(mygen))
# print (next(mygen))
# print (next(mygen))
# print (next(mygen))
# print (next(mygen))
# print (next(mygen))
# print (next(mygen))
# print (next(mygen))
# name="maruthu pandiyan"
# myname=iter(name)
# print (next(myname))
# print (next(myname))
# print (next(myname))
# print (next(myname))
#
# def febi(n):
#     a=1
#     b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# mylist=[]
# for i in febi(100):
#     mylist.append(i)
# print (mylist)



# import matplotlib.pyplot as myplot
#
# myplot.figure(figsize=(5,5))
# num=[2,3,6,8,9]
# value=["agri","own business","IT","Govt","Joint"]
# myplot.pie(num,labels=value,autopct="%.1f%%")
#
#
# myplot.show()
#
# import math
# def myfun(n):
#     print ("%.f"%math.pi)
# myfun(10)
# import sys
# print (sys.version_info[0])
# def fact(n):
#     if not n:
#         return 1
#     return n*fact(n-1)
# print (fact(1))
# from decimal import *
# import math
# k=10
# k+=1
# getcontext().prec=k
# print (k)
# n=142314.45555588
# Decimal(n)
# print (Decimal(n))
#
# import math,sys
# from decimal import *
#
# def fact(n):
#     if not n:
#         return 1
#     return n*fact(n-1)
#
# def getiterate_value(k):
#     k+=1
#     getcontext().prec=k
#     sum=0
#     for k in range(k):
#         first=fact(6*k)*(13591409+545140134*k)
#         down=fact(3*k)*(fact(k))**3*(640320**(3*k))
#         sum+=first/down
#     return Decimal(sum)
#
# def getvalueof_pi(k):
#     iter=getiterate_value(k)
#     up = 426880 * math.sqrt(10005)
#     pi = Decimal(up) / iter
#     return pi
#
# def shell():
#     while True:
#         print (">>> ",end='')
#         entry=input()
#         if entry == "quit":
#             break
#         if not entry.isdigit():
#             print ("You did not enter number,Try Again")
#         else:
#             print(getvalueof_pi(int(entry)))
#
# if __name__=="__main__":
#     shell()
# import math
# def nthofe(k):
#     return "%.*f"%(k,math.e)
# if __name__=="__main__":
#     correction=False
#     while not correction:
#         print (">>> Number can be 1 to 52")
#         print (">>>",end='')
#         number=int(input("Enter Number: "))
#         if number<=52 and number>0:
#             correction=True
#     print (nthofe(number))

# def febbi():
#     while True :
#         print (">>>Enter Your Number: ",end='')
#         try:
#             febbi_number=int(input())
#             break
#         except:
#             print ("Try Again!")
#             continue
#
#     a=1
#     b=1
#     output=[]
#     febbi_number+=1
#     for i in range(febbi_number):
#         output.append(a)
#         a,b=b,a+b
#     return output
# if __name__=="__main__":
#     print (febbi())
# print ()
# print ()
# def fibSequence(n):
#     """
#     Generates a fibonacci sequence
#     with the size of n
#     """
#     assert n > 0
#
#     series = [1]
#
#     while len(series) < n:
#         if len(series) == 1:
#             series.append(1)
#         else:
#             series.append(series[-1] + series[-2])
#
#     for i in range(len(series)):  # Convert the numbers to strings
#         series[i] = str(series[i])
#
#     return(', '.join(series))  # Return the sequence seperated by commas
#
#
# def main():  # Wrapper function
#
#     print(fibSequence(int(input('How many numbers do you need? '))))
#
# if __name__ == '__main__':
#     main()
# factors=lambda n: [x for x in range(1,n+1) if not n%x]
# print factors(20)
# factor=lambda n:[x for x in range(1,n+1) if not n%x ]
# isprime=lambda n:len(factor(n))==2
# primefactor=lambda n:list(filter(isprime,factor(n)))
# print primefactor(50)
# print (factor(50))

factors = lambda n: [x for x in range(1, n + 1) if not n % x]
is_prime = lambda n: len(factors(n)) == 2
primefactors = lambda n: list(filter(is_prime, factors(n)))


def primeFactorize(n):
    n = int(n)
    f = primefactors(n)
    # print (f)
    if is_prime(n):
        return str(n)
    else:
        return str(f[0]) + "*" + primeFactorize(n / f[0])


if __name__ == '__main__':
    print ("Welcome to the Prime Factorizer.. Enter the numbers in the prompt or enter 'quit' to exit")
    num = 0

    while True:
        if num:
            print(primeFactorize(num))
        print(">>>",end='')
        num = input()
        if num == "quit":
            break
# quit
# factor=lambda n:[x for x in range(1,n+1) if not n%x]
# # print (factor(12))
# isprime=lambda n:len(factor(n))==2
# print(isprime(3))
# primefactor=lambda n:list(filter(isprime,factor(n)))
# def findprimefactor(n):
#     n=int(n)
#     f=primefactor(n)
#     if isprime(n):
#         return str(n)
#     else:
#         return str(f[0])+ "*" +findprimefactor(n/f[0])
# if __name__=="__main__":
#     print ("here we are checking prime factor for your input, to exit enter quit...")
#     inpt=0
#     while True:
#         if inpt:
#             print (findprimefactor(inpt))
#         print (">>>",end='')
#         inpt=input()
#         if inpt=="quit":
#             break
# def nexprime(n):
#     prime=[]
#     for i in range(2,n+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             prime.append(i)
#     return prime
# if __name__=="__main__":
#     print("Please enter your number for prime find: ")
#     print (">>>",end='')
#     num=int(input())
#     prime=(nexprime(num))
#     length=len(nexprime(num))
#     n=0
#     while length>0:
#         next=input("Type Next for next Prime: ").lower()
#         if next=="next":
#             print (prime[n])
#             n+=1
#             length=length-1
#         else:
#             print ("Bye..")
#             break
#
#
#
#"""
#Find Cost of Tile to Cover W x H Floor
#Calculate the total cost of tile it would take to cover a floor plan of
#width and height, using a cost entered by the user.
#"""
# costToCover = lambda w,h,ppm: w*h*ppm
# print(costToCover(50,100,0.5))
#
# """
# Find max combination of 2 numbers in a sequence - n^2
# """
# def find_max_comb(seq):
#     temp = 0
#     for i,n in enumerate(seq):
#         for v in seq[i+1:]:
#             temp = max(temp,n+v)
#         print (i)
#         print (n)
#     return temp
#
# print(find_max_comb([1,7,3,1,3,6,4]))
#
# import socket
# import sys
#
#
# def connect_to_ip(ip, port):
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((ip, port))
#         return sock
#
#     except Exception:
#         return None
#
#
# def scan_port(ip, port, timeout):
#     socket.setdefaulttimeout(timeout)
#     sock = connect_to_ip(ip, port)
#
#     if sock:
#         print('Able to connect to: {0}:{1}').format(ip, port)
#         sock.close()
#     else:
#         print('Not able to connect to: {0}:{1}').format(ip, port)
#
#
# # Get the IP / domain from the user
# ip_domain = raw_input("Enter the ip or domain: ")
# if ip_domain == '':
#     print('You must specify a host!')
#     sys.exit(0)
#
# # Get the port range from the user
# port = raw_input("Enter the port range (Ex 20-80): ")
# if port == '':
#     print('You must specify a port range!')
#     sys.exit(0)
#
# # Optional: Get the timeout from the user
# timeout = raw_input("Timeout (Default=5): ")
# if not timeout:
#     timeout = 5
#
# port_range = port.split("-")
#
# # Get the IP address if the host name is a domain
# try:
#     ip = socket.gethostbyname(ip_domain)
# except Exception:
#     print('There was an error resolving the domain')
#     sys.exit(1)
#
# # If the user only entered one port we will only scan the one port
# # otherwise scan the range
# if len(port_range) < 2:
#     scan_port(ip, int(port), int(timeout))
# else:
#     for port in range(int(port_range[0]), int(port_range[1])+1):
#         scan_port(ip, int(port), int(timeout))
