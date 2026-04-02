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
            
def visa_alla_citat(citatlista):
    if len(citatlista) == 0:
        print("Det finns inga citat")
    else:
        for index, citat in enumerate(citatlista):
            print(f"{index + 1}. {citat.strip()}")
    
def lagg_till_citat(citatlista):
    citat = input("Skriv ett citat: ")
    forfatter = input("Skriv författaren: ")
    
    if citat == "" or forfatter == "":
        print("Du måste skriva både citat och författare!")
        return False
    
    ny_rad = f'"{citat}" - {forfatter}\n'
    citatlista.append(ny_rad)
    print("Citatet lades till!")
    return True

def slumpa_citat(citatlista):
    if len(citatlista) == 0:
        print("Inga citat finns än!")
    else:
        slumpmassigt = random.choice(citatlista)
        print(f"Slumpmässigt citat: {slumpmassigt.strip()}")

def huvudprogram():
    filnamn = "citat.txt"
    citatlista = ladda_citat_fran_fil(filnamn)
    
    while True:
        print("\n1. Visa alla citat")
        print("2. Lägg till nytt citat")
        print("3. Visa slumpmässigt citat")
        print("4. Avsluta")
        
        val = input("\nVälj: ")
        
        if val == "1":
            visa_alla_citat(citatlista)
        elif val == "2":
            lagg_till_citat(citatlista)
            spara_citat_till_fil(citatlista, filnamn)
        elif val == "3":
            slumpa_citat(citatlista)
        elif val == "4":
            print("Hejdå!")
            break
        else:
            print("Ogiltigt val, försök igen!")

if __name__ == "__main__":
    huvudprogram()