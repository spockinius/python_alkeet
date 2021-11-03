# Täysi-ikäisyyden ehtolauseke
ikä = int(input("Kuinka vanha olet?"))
if ikä >= 18:
    print("Olet täysi-ikäinen!")
else:
    print("Et ole täysi-ikäinen!")

# Suurempi tai yhtä suuri luku
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
 
if luku1 > luku2:
    print("Suurempi luku:", luku1)
elif luku2 > luku1:
    print("Suurempi luku:", luku2)
else:
    print("Luvut ovat yhtä suuret!")

# Kumpi on vanhempi
nimi1 = input("Nimi: ")
ikä1 = int(input("Ikä: "))
nimi2 = input("Nimi: ")
ikä2 = int(input("Ikä: "))

if ikä1 > ikä2:
    print(f"Vanhempi on {nimi1}")
elif ikä2 > ikä1:
    print(f"Vanhempi on {nimi2}")
else:
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")

# Aakkosjärjestyksessä viimeinen
sana1 = input("Anna 1. sana: ")
sana2 = input("Anna 2. sana: ")

if sana1 < sana2:
    print(f"{sana2} on aakkosjärjestyksessä viimeinen.")
elif sana1 == sana2:
    print("Annoit saman sanan kahdesti.")
else:
    print(f"{sana1} on aakkosjärjestyksessä viimeinen.")

 # Keittoa vai ei
nimi = input("Mikä on nimesi: ")

if nimi != "Jerry":
    keittomäärä = int(input("Kuinka monta annosta keittoa: "))
    print(f"Kokonaishinta on {5.90*keittomäärä}")
    print("Seuraava!")

if nimi == "Jerry":
    print("Seuraava!")   

# Suuruusluokka
luku = int(input("Anna luku 1: "))
 
if luku < 1000:
    print("Luku on pienempi kuin 1000")
 
if luku < 100:
    print("Luku on pienempi kuin 100")
 
if luku < 10:
    print("Luku on pienempi kuin 10")
 
print("Kiitos!")

# Laskin
luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
komento = (input("Komento: "))

if komento == "summa":
    print(f"{luku1} + {luku2} = {luku1+luku2}")

if komento == "tulo":
    print(f"{luku1} * {luku2} = {luku1*luku2}")

if komento == "erotus":
    print(f"{luku1} - {luku2} = {luku1-luku2}")

if komento != "summa" or komento != "tulo" or komento != "erotus":
    print()


        

