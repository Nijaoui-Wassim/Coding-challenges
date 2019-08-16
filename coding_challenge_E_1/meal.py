from time import gmtime, strftime
import os
import sys

timeleft =[]
ind = ''


def get_current_time():
    global timeleft
    global ind
    x = int(strftime("%H", gmtime())) #Hours
    y = int(strftime("%M", gmtime())) #Minutes
    #format time
    if x > 12:
        ind = 'pm'
        x = x-12
    else:
        ind = 'am'
    if x > 7:
        timeleft += [12-x-1]
        timeleft += [60-y]
    else:
        timeleft += [7-x-1]
        timeleft += [60-y]        
        


def show():
    global timeleft
    global ind
    print('time_to_eat("'+ strftime("%H:%M", gmtime()) + ind + ' ") ➞ ', timeleft)
    print('Time ', timeleft[0] + 1 + int(strftime("%H", gmtime())), 'h')


def send_request():
    while True:
        x = input('run? Y or N  ')
        if x.upper()=='Y':
            break
        else:
            sys.exit()

            
def structure():
    while True:
        send_request()
        get_current_time()
        show()

structure()
