import sys


Range = ['EXCEL', 'LOG - Excel','MOBILE', 'MOB - Autre','OUTLOOK', 'LOG - Outlook','BELL','ACC - Portail Bell',
         'WORKDAY','APP - Workday','SHAREPOINT','APP - SPOL','SPOL', 'APP - SPOL','CASQUE FOCUS','MAT - Casque Focus',
         'IPHONE','MAT - iPhone','AIRWATCH','MOB - AirWatch','HUB' ,'PUBLIC','ACC-WIfi VIsiteur','MOB - AirWatch',
         'MUREX','ACC - MUR','SUIVI','DEM - Suivi REQ','BRISÉ''MOB - Bris','OKTA','ACC - Mot De Passe OKTA','CELLULAIRE',
         'MOB - Autre','CELL','MOB - Autre','IMPRIMANTE','MAT - Imprimante','IMPRESSION','MAT - Imprimante','IMPRIMER',
         'MAT - Imprimante','BCT','APP - BCT','BELL CONNEXION','APP - BCT','BTC','APP - BCT','VC','MM - VC','VIDÉOCONFÉRENCE','MM - VC',
         'PRÉSENTATION','MM - Présentation','IPAD','MAT - Ipad','MUREX','ACC - MUR''ÉQUIPEMENT','MAT - Autre','MATERIEL',
         'MAT - Autre','CABLE','MAT - Autre','CÂBLE','MAT - Autre','CABLES','MAT - Autre','ANDROID','MAT - Samsung','SAMSUNG',
         'MAT - Samsung','PORTABLE','MAT - Portable','ORDINATEUR','MAT - Portable','SURFACE','MAT - Surface','TABLETTE',
         'MAT - Surface','CLAVIER','MAT - Clavier','SOURIS','MAT - Souris','TOUCHPAD','MAT - Souris','TOUCHSCREEN','MAT - Portable',
         'JETON','MAT - Jeton RSA','VPN','MAT - Jeton RSA','RSA','MAT - Jeton RSA','DISTANCE','MAT - Jeton RSA','WIFI','ACC - WiFi','5G','ACC - WiFi','GED','LOG - Documentum','DOCUMENTUM','LOG - Documentum',
         'ANTIDOTE','LOG - Antidote','ANTIOPS','LOG - Antidote','HARMONIE','LOG - Harmon.ie','CAPITAL','LOG - Capital IQ','IQ',
         'LOG - Capital IQ','EXPLORER','LOG - Internet Explorer','IE','LOG - Internet Explorer','CHROME','LOG - Autre','ÉCRAN',
         'MAT - Moniteur','MONITEUR','MAT - Moniteur','STATION',"MAT - Station D'accueil",'DOC',"MAT - Station D'accueil",'ONENOTE',
         'LOG - One Note','ONE NOTE','LOG - One Note','ONEDRIVE','LOG - One Drive','DNS','INFRA - DNS','ONE DRIVE','LOG - One Drive',
         'WORD','LOG - Word','PDF','LOG - PowerPDF','NUANCE','LOG - PowerPDF','INFORMATION','DEM - Information','OKTA','ACC - Mot De Passe OKTA',
         'COMPTE','ACC - Mot De Passe AD','LIGNE','FIL - Ligne','IP','INFRA - Réseau Filaire','SERVEUR','INFRA - Serveur',
         'SERVER','INFRA - Serveur','DYNAMICS','APP - DAX','DAX','APP - DAX','POWERPOINT','LOG - Power Point','POWER POINT','LOG - Power Point',
         'PAPERCUT','MAT - Imprimante','COURRIEL','LOG - Outlook','PRINTER','MAT - Imprimante','POSTE','MAT - Portable','TEAMS','LOG - Teams',
         'THINKCELL','LOG - ThinkCell','THINK','LOG - ThinkCell','CONCUR','APP - CONCUR','[JUNK','SEC - Hameçonnage','Hameçonnage','SEC - Hameçonnage']
Texte = ''
TAG = ''


def gettexte():
    global Texte
    Texte = input('what should I analyse?(press exit to quit)   ')
    if Texte.upper() =='EXIT':
        sys.exit()
    Texte = Texte.split()

def analyse(Texte):
    global Range,TAG
    for i in Texte:
        if i.upper() in Range:
            TAG = Range[Range.index(i.upper())+1]
            break
        elif TAG =='' or TAG =='kiosque - kiosque':
            TAG ='kiosque - kiosque'
    print ('here is the TAG  \n',TAG)

def init():
    global TAG,Texte
    TAG =''
    Texte = ''
    


def running():
    global Texte
    while True:
        gettexte()
        analyse(Texte)
        init()

running()
