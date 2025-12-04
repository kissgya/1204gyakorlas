#2. feladat – Kérj be egy N számot, és számold ki az 1-től N-ig terjedő számok szorzatát (faktoriális ELLENTÉTE: itt nem csak N!, hanem általánosan 1·2·3…·N).

szam = int(input("Addj meg egy számot: "))

tarolo = 1
for i in range(1,szam+1):
    tarolo = tarolo * i

print(f"1-től {szam}-ig terjedő számok szorzata = {tarolo}")