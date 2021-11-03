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