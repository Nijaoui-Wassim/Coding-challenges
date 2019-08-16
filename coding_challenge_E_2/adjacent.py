
lista = []

def getlist():
    global lista
    while True:
        x = input('give me a char  ')
        if len(x) == 1:
            lista += x.upper()
        if x =='':
            break

def verif(List):
    listb = []
    for i in range(len(List)-2):
        if List[i] != List[i+1]:
            listb += List[i]
            if List[i] == List[i-1]:
                listb.remove(List[i])
            print(listb)

getlist()
print(lista)
verif(lista)

