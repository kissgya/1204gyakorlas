#9. feladat – OOP + lista: Tanulók kezelése

#Student osztály: név, életkor, átlag.
#Kérj be 3 tanulót, tedd őket listába, majd írd ki annak a nevét, akinek a legjobb az átlaga.

'''
class Student():
    students=[]
    
    def __init__(self, nev, eletkor, atlag):
        self.name=nev
        self.age=eletkor
        self.average=atlag
        self.students.append(self)

        max = self.students[0].average
        id = 0
        
        for i in range(len(self.students)):
            if self.students[i].average > max:
                max=self.students[i]
                id=i

        print(self.students[id].name)


for i in range(3):
    nev=input(f"Kérem a(z) {i}. nevet: ")
    elektor=int(input(f"Kérem a(z) {i}. életkort: "))
    atlag=float(input(f"Kérem a(z) {i}. átlagot: "))
    student =Student(nev, elektor, atlag)
    



tanulo1=Student("Takács Tamás", "20", "4.4")
tanulo2=Student("Gipsz Jakab", "22", "4.6")
tanulo3=Student("Molnár Melinda", "27, "5.0")
'''

#A felső kikommentelt a tanár verziója, az alábbi meg chatgpt
class Student:
    def __init__(self, nev, eletkor, atlag):
        self.name = nev
        self.age = eletkor
        self.average = atlag


students = []   # üres lista a tanulóknak

# 3 tanuló bekérése
for i in range(3):
    nev = input(f"Kérem a(z) {i+1}. tanuló nevét: ")
    eletkor = int(input(f"Kérem a(z) {i+1}. tanuló életkorát: "))
    atlag = float(input(f"Kérem a(z) {i+1}. tanuló átlagát: "))
    
    student = Student(nev, eletkor, atlag)
    students.append(student)


# Legjobb átlag keresése
best = students[0]
for s in students:
    if s.average > best.average:
        best = s

print(f"A legjobb átlagú tanuló: {best.name}, átlaga: {best.average}")