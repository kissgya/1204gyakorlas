#4. feladat – Számjegyek összege
#Kérj be egy számot, majd számold ki a számjegyeinek összegét.

szam = int(input("Adj meg egy számot: "))

osszeg = 0
temp = abs(szam)

while temp > 0:
    osszeg = osszeg + (temp % 10)
    temp //= 10

print("A számjegyek összeg:", osszeg)



szam = input("Adj meg egy számot: ")

osszeg = 0

for i in range(len(szam)):
    osszeg = osszeg + int(szam[i])

print(f"A számjegyek összege: {osszeg}")
