import os
#import math

Board = ['_','_','_','_','_','_',' ',' ',' ']
flip = 'X'


def show():
    for i in (0,3,6):
        print(Board[i], '|', Board[i+1],'|', Board[i+2])
        
def turn():
    global flip
    global Board
    for s in range(10):
        checkerall()
        if s==9:
            print('DRAW')
        while True:
            p = int(input ())
            if Board[p-1] != 'X' and Board[p-1] != 'O' and p>0 and p<10:
                break
        if flip =='X':
            Board[p-1] = 'X'
            flip = 'O'
            print (" \n" * 10)
            show()
        else:
            Board[p-1] = 'O'
            flip = 'X'
            print (" \n" * 10)
            show()
            
def checkerH():
    global flip
    for i in (0,1,2):
        if Board[i] == Board[i+3]and Board[i+3] == Board[i+6]:
            if flip =='X' and Board[i] == 'X':
                print('X player Win')
                return
            elif flip =='O' and Board[i] == 'O':
                print('O player Win')
                return
def checkerV():
    global flip
    for i in range(0,3,6):
        if Board[i] == Board[i+1]and Board[i+1] == Board[i+2]:
            if flip =='X' and Board[i] == 'X':
                print('X player Win')
                return
            elif flip =='O' and Board[i] == 'O':
                print('O player Win')
                return
def checkCr():
    global flip
    if Board[0] == Board[4]and Board[4] == Board[8]:
        if flip =='X' and Board[i] == 'X':
            print('X player Win')
            return
        elif flip =='O' and Board[i] == 'O':
            print('O player Win')
            return
    if Board[2] == Board[4]and Board[4] == Board[6]:
        if flip =='X' and Board[i] == 'X':
            print('X player Win')
            return
        elif flip =='O' and Board[i] == 'O':
            print('O player Win')
            return
def checkerall():
    checkerV()
    checkerH()
    checkCr()
        
show()
turn()
    
