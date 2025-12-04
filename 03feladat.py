#3. feladat – Prímszám ellenőrzése
#Döntsd el egy számról, hogy prímszám-e (szelekció + iteráció).

szam = int(input("Adj meg egy egész számot: "))
prim = True

if szam < 2:
    prim = False
else:
    for i in range(2, int(szam**0.5)+1):
        if szam % i == 0:
            prim = False
            break

if prim == True:
    print("A megadott szám prímszám.")
else:
    print("A megadott szám NEM prímszám.")