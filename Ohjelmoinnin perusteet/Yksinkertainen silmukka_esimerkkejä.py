# Jatketaanko vai ei?
while True:
    print("moi")
    jatketaanko = input("Jatketaanko? ")
    if jatketaanko == "ei":
        print("ei sitten")
        break

from math import sqrt
# Neliöjuuri, syötä luku
while True:
    luku = int(input("Syötä luku: "))

    if luku < 0:
        print("Epäkelpo luku")
    
    elif luku > 0:
        print(sqrt(luku))

    elif luku == 0:
        print("Lopetetaan...")
        break          

# Lähtölaskenta
luku = 5
print("Lähtölaskenta!")
while True:     
    print(luku)

    luku = luku - 1

    if luku == 0:
        break
       
print("Nyt!")       

# Salasanan syöttäminen
salasana = input("Salasana: ")
while True:
    toista = input("Toista salasana: ")

    if toista != salasana:
        print("Ei ollut sama!")
    
    elif salasana == salasana:
        break
    
print("Käyttäjätunnus luotu!")

# Kysy pin-koodi, laske yritykset
yritykset = 1
koodi = 4321
while True:
    koodi = int(input("PIN-koodi: "))
    
    if koodi == 4321:
        if yritykset == 1:
            print("Oikein, tarvitsit vain yhden yrityksen!")
            break

        if yritykset > 1:
            print(f"Oikein, tarvitsit {yritykset} yritystä")
            break
    
    if koodi != 4321:
        print("Väärin")
        yritykset = yritykset + 1

# Milloin on seuraava karkauspäivä
vuosialk = int(input("Vuosi: "))
vuosiuusi = vuosialk
while True:

    vuosiuusi = vuosiuusi + 1

    if vuosiuusi % 100 == 0:
        if vuosiuusi % 400 == 0:
            print(f"Vuotta {vuosialk} seuraava karkausvuosi on {vuosiuusi}")
            break
           
    elif vuosiuusi % 4 == 0:
        print(f"Vuotta {vuosialk} seuraava karkausvuosi on {vuosiuusi}")
        break      
    
    else:
        continue

# Tarina annetuista sanoista
sanat = ""
edellinen_sana = ""
while True:
    sana = input("Anna sana: ")

    if sana == "loppu":
        break
    
    if sana == edellinen_sana:
        break
    
    sanat += sana + " "

    edellinen_sana = sana

print(sanat)
