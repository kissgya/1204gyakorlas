#1. feladat – Faktoriális számítása ciklussal
#Kérj be egy számot, és számold ki a faktoriálisát iterációval.

szam = int(input("Adj meg egy egész számot: "))

faktorialis = 1
for i in range(1,szam+1):
    faktorialis = faktorialis * i

print(f"{szam}! = {faktorialis}")