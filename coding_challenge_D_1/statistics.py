import copy
import math

mylist = []
showlist = []

def mode(somelist):
    somelist = copy.copy(mylist)
    somelist.sort()


def getlist():
    global mylist
    while True:
        number = input('Give me a number (enter nothing to finish) ')
        if number =='':
            break
        mylist.append(int(number))

def show(somelist):
    global mylist
    global showlist
    print('mode(',somelist, ') ➞ ', showlist)

def counter(somelist):
    global showlist
    current = 0
    for i in range(len(somelist)-3):
        if somelist[i] == somelist[i+1]:
            current = somelist[i]
            showlist.append(current)
            del somelist[i+1] # delete the reccurents values

                
            

getlist() #get the list
mode(mylist) #copy & sort the list
counter(mylist) #add values to the Results and delete reccurent values
show(mylist) #show the final list
            
