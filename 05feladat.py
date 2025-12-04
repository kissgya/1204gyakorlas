#5. feladat – Lista elemeinek négyzetre emelése
#Adott egy lista, készíts új listát, amely minden elem négyzetét tartalmazza.

lista1 = [2,5,3,8,9,1]
lista2 = []

for i in range(len(lista1)):
    lista2.append(lista1[i]**2)

print(f"A lista számainak négyzetre emelt értékei: {lista2}")