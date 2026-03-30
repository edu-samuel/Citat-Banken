import random

def ladda_citat_fran_fil(filnamn):
    try:
        with open(filnamn,"r", encoding="utf-8")as fil:
            return fil.readlines()
    except FileNotFoundError:
        return []
    
def spara_citat_till_fil(citatlista, filnamn):
    with open(filnamn, "w",encoding="utf-8")as fil:
        for citat in citatlista:
            fil.write(citat)

def 