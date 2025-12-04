#6. feladat – Szótár gyakorlás
#Kérj be 5 nevet és életkort, majd tárold őket egy dict-ben.
#Ezután írd ki a legidősebb személy nevét.

emberek = {}

for i in range(5):
    nev = input("Kérem a nevet: ")
    kor = int(input(f"Kérem {nev} korát: "))
    emberek[nev] = kor

legidosebb_neve = max(emberek, key=emberek.get)
legidosebb_kora = emberek[legidosebb_neve]

print(f"A legidősebb személy: {legidosebb_neve}, {legidosebb_kora} éves.")