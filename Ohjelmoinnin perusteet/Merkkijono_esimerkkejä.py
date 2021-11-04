
# Täytä sanasta jäävä tyhjä tila
sana = input("Sana: ")
sananpituus = len(sana)
tähdet = 20 - sananpituus

print(str(tähdet*"*") + sana)

# Tulosta sanoja peräkkäin
sana = input("Anna merkkijono: ")
määrä = int(input("Anna määrä: "))

print(sana*määrä)

# Kumpi merkkijono on pidempi
jono1 = input("Anna jono 1: ")
jono2 = input("Anna jono 2: ")

if len(jono1) > len(jono2):
    print(f"{jono1} on pidempi")

elif len(jono1) < len(jono2):
    print(f"{jono2} on pidempi")

else:
    print("Jonot ovat yhtä pitkät")

# Kirjaimet väärinpäin
sana = input("Anna merkkijono: ")
kirjain = -1
pituus = len(sana)*-1

while kirjain >= pituus:
    print(sana[kirjain])
    kirjain = kirjain - 1

# Vertaa sanan sisällä olevia kirjaimi
sana = input("Anna sana: ")
if (sana[1]) == sana[len(sana) - 2]:
    print(f"Toinen ja toiseksi viimeinen kirjain on {sana[1]}")
else:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")

# Risuaitojen määrä
määrä = int(input("Leveys: "))
arvo = "#"

print(määrä*arvo)

# Tähtilaatikko sanan ympärille
sana = input("Sana: ")
sanamäärä = len(sana)
puolikas = len(sana)//2

ekarivi = 30 * "*"
tokarivi_alku = "*" + (14 - puolikas) * " " + sana
tokarivi_alku_len = len(tokarivi_alku)
tokarivi_loppu = (29 - tokarivi_alku_len) * " " + "*"
vikarivi = 30 * "*"

print(ekarivi)
print(tokarivi_alku + tokarivi_loppu)
print(vikarivi)