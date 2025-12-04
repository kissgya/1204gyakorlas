#7. feladat – OOP: Egyszerű Osztály – Auto
#Hozz létre egy Auto osztályt, amely attribútumai: márka,típus,évjárat
#Az osztály tartalmazzon metódust, ami kiírja a teljes adatot szép formában.


class Auto:
    def __init__(self, marka, tipus, evjarat):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat

    def kiiratas(self):
        print(f"Autó adatai: Márka: {self.marka}, Típus: {self.tipus}, Évjárat: {self.evjarat}")


autok = []

for i in range(3):
    marka = (input("Adja meg az autó márkáját: "))
    tipus = (input("Adja meg az autó típusát: "))
    evjarat = (int(input("Adj meg az autó évjáratát: ")))

    auto =Auto(marka, tipus, evjarat)
    autok.append(auto)

for auto in autok:
    auto.kiiratas()


        