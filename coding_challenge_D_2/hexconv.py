import math

stringtext = ''
hextext = ''

def show(sometext):
    global hextext
    global stringtext
    print('convert_to_hex("'+stringtext+'") ➞ "' + hextext+'"')

def convert(sometext):
    global hextext
    for i in sometext:
        hextext += (' ' + format(ord(i), "x"))
        


def gettext():
    global stringtext
    stringtext = input('give me a text to convert   ')

gettext() 
convert(stringtext)
show(stringtext)
