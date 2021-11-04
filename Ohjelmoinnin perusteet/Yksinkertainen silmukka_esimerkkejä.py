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

# Lukujen summa, keskiarvo ja määrä
luku = 0
yhteensä = 0
yhteensä_pos = 0
yhteensä_neg = 0
summa = 0
keskiarvo = 0
while True:
    luku = int(input("Syötä kokonaislukuja, 0 lopettaa: "))

    if luku > 0:
        yhteensä += 1
        yhteensä_pos += 1
    if luku < 0:
        yhteensä += 1
        yhteensä_neg += 1
    
    if luku != 0:
        summa = summa + luku

    if luku == 0:
        break

print("Syötä kokonaislukuja, 0 lopettaa:")
print(f"Lukuja yhteensä {yhteensä}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {summa/yhteensä}")
print(f"Positiivisia {yhteensä_pos}")
print(f"Negatiivisia {yhteensä_neg}")

# Ehto silmukassa, tulosta luvut
luku = 0
while luku < 30 and luku % 2 == 0:
    luku += 2
    print(luku)

# Lähtölasku
print("Valmiina?")
luku = int(input("Anna luku: "))
while luku > 0:
    print(luku)
    luku -= 1
print("Nyt!")

# Kirjoita lukua tiettyyn pisteeseen asti
alkluku = int(input("Mihin asti: "))
luku = 1
while luku != alkluku:
    print(luku)
    luku = luku + 1

# Kahden potenssi
asti = int(input("Mihin asti: "))
luku = 1
while luku <= asti:
    print(luku)
    luku = luku*2

# Kahden potenssi muuttuvalla kertoimella
asti = int(input("Mihin asti: "))
kerroin = int(input("Mikä kerroin: "))
luku = 1
while luku <= asti:
    print(luku)
    luku = luku*kerroin

# Kirjoita ratkaisu tähän
asti = int(input("Mihin asti: "))
luku = 1
summa = 0

# Peräkkäisten lukujen summa
asti = int(input("Mihin asti: "))
luku = 1
summa = 0

while summa < asti:
    summa = summa + luku
    luku = luku + 1

print(summa)


