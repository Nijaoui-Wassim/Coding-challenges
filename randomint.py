import random
import math


#___________________________________________
numbers = []
allthem = 0
moy = []
a = 0 ; s=0
j= int(input('How many times should I run?  '))
c= int(input('How many numbers?  '))
minn= int(input('MIN  '))
maxn= int(input('MAX  '))

#___________________________________________
def getdataset():
    global numbers, c, s, minn, maxn
    i=0; counter=0; s=0
    while True:
        counter +=1
        i = random.randint(minn,maxn)
        numbers.append(i)
        if counter == c:
            break

#___________________________________________

def search():
    global numbers, allthem
    allthem = 0
    for i in numbers:
        for p in range (i+1,len(numbers)-1):
            if numbers[i] == numbers[p]:
                allthem +=1

#___________________________________________                
  
def moyenne():
    global s, moy, maxn
    for i in range(len(moy)-1):
         s += moy[i]/maxn
    print(s/(len(moy)/maxn/100/j))

#___________________________________________

def running():
    global j
    for i in range(j):
        getdataset()
        search()
        #print (allthem)
        moy.append(allthem) #add values to the list
        moyenne()

#___________________________________________

running()
print(moy)
print('How random? ',s, '%')
