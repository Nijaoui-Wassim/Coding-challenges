
progress_days = []
days = []


def getdays():
    global days
    numdays = int(input('How many days? '))
    for i in range (numdays):
        days += [input('progress value ')]


def getprogress():
    global days
    global progress_days
    for i in range (1,len(days)):
        if int(days[i-1]) < int(days[i]):
            progress_days += days[i]


def show():
    global days
    global progress_days
    print(days, " => ",len(progress_days))


        
getdays()
getprogress()
show()
