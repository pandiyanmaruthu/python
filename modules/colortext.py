# from colorama import init
# init()
# from colorama import Back
# # print (Fore.RED+ "Hello Pycharm")
# print (not Back + "Hello Pycharm")
import openpyxl
import os
print (os.getcwd())
os.chdir("/home/maruthu")
print (os.getcwd())
with open("Downloads/db.xlsx","r") as xls:
    d=xls.readlines()
    for i in d:
        print i
# with open("Downloads")
