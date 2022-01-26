#Kod wpiszesz 


#imie 
# nazwisko
# zespół F1
# Partner 
# Tor Wyścigowy

# F1 = input( "Wpisz imie:", "Wpisz nazwisko:", "Wpisza zespol:" , "Wpisza partner:" , "Wpisz Tor:")


#Mulitle line input
#imie, nazwisko = input("Enter two values: ").split()

def WhichTeam(name): #def - definuje FUNKCJE, która może być póxniej reużywalna albo 
    if(imie == "lando"): 
        zespol = "Mclaren"
    elif(imie == "lewis"):      
        zespol = "Mercedes"
    elif(imie == "valteri"):
        zespol = "Alfa"
    elif(imie == "daniel"):
        zespol = "Mclaren"
    elif(imie == "zhau"):
        zespol = "Alfa"
    else:
        zespol = "Other Team"
    return zespol

for x in range(1, 4): 
    imie = input("Imie: ").lower()
    print( str(x) + " Kierowca:")
    print(WhichTeam(imie))



#LOO


