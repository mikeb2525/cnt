# Task 1
import sys
class Assignment2:

    def _init_(self, age):
        self.age = age

# Task 2
    def sayWelcome(self, name):
        sys.stdout.write("Welcome to the assignment, %s! Haven't seen you in %s years!\n" % (self.name(), self.age))


# Task 3

    def doubleList(list):

        newList = []

        for name in list:
            newName = name * 2
            newList.append(newName)
        newList.reverse()
        print(newList)


#Task 4

    def modifyString(str):
        position = 3-1
        index = 0

        len_list = (len(str))

        index = (position + index)%len_list
        print(str.toUpper(index))


#Task 5

import re

def isGoodPassword():
    passWord = input("Input your password: ")
    x = True
    while x:
        if(len(passWord)< 9):
            break

         elif not re.search("[a-z]" > 3, passWord):
             break

         elif not re.search("[$#@!%^&*]", passWord) or not re.search("[0-9]", passWord):
             break


         else:
         print(x)
         x = False
         break

     if x:
      print(x)


#Task 6

from socket import *

def connectTcp(host, port):
     try:

          s = socket(AF_INET, SOCK_STREAM)

          host_address = gethostbyname(host)

          s.connect((host_address, port))

          s.close()

          return True
     except:

          return False

retVal = connectTcp("www.google.com", 80)

if retVal:
     print("Connection established correctly")
else:
     print("Some error")


