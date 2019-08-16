import math
#import copy
import random

password = ''
holdpass = ''
currentkey = []
currentlen = []
revpass = ''

def verification(Password):
    if len(Password)>8 and Password != '123456789':
        return True

def getpass(): #get the input
    global password
    while True:
        password = input('give me a password  ')
        #verification(password)
        if verification(password): #add a verification layer
            break


def enclayer1(): #encrypt the password
    global password
    global currentkey
    global holdpass
    for i in range(len(password)-1):
        randomizer = random.randint(1,10)
        currentkey.append(randomizer)
        
        if password[i].isalpha():
            holdpass += str(ord(password[i])*randomizer).replace(' ', '')
        else:
            holdpass += str(int(password[i])*randomizer).replace(' ', '')
                    
    

def showpass():
    global password
    holder =''
    print('Secret Key')
    for i in range(len(currentkey)-1):
        holder += str(currentkey[i])
    print(holder)
    print('This is the crypted password ')
    print(holdpass)



#Run script
getpass()
enclayer1()
showpass()


