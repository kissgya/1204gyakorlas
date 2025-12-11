'''
10. feladat – OOP: Öröklődés

Készíts egy Allat alaposztályt (név, életkor).
Készíts két leszármazottat:

Kutya (plusz: fajta)

Macska (plusz: szín)

Mindkettőnek legyen hang() metódusa, ami kiírja a saját hangját.
Példányosítsd őket és hívd meg a metódust.

'''

class Allat:
    def __init__(self, nev, kor):
        self.name=nev
        self.age=kor

class Kutya(Allat):
    def __init__(self, nev, kor, fajta):
        super().__init__(nev, kor)
        self.type=fajta

    def hang(self):
        print(f"{self.name} mondja: Vau-vau")

class Macska(Allat):
    def __init__(self, nev, kor, szin):
        super().__init__(nev,kor)
        self.color=szin

    def hang(self):
        print(f"{self.name} mondja: Miau")

kutya = Kutya("Dió", 8, "Beagle")
kutya.hang()

macska = Macska("Luca", 3, "Házi")
macska.hang()