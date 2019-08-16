import math
import random

def checker():
    x1 = int(input('give min '))
    x2 = int(input('give max '))
    y = random.randint(x1,x2)
    counter = 0
    while True:
        counter += 1
        while True:
            print('give me a number between 1 and 10 - this is attempt number ', counter)
            x = int(input())
            if float(x).is_integer():
                break
        if x == y:
            print('winner')
            break
        elif x>y:
                print ('too hight')
        else:
            print ('too low')            

checker()

