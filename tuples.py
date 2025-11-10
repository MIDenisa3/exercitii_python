# 1.Parcurge un tuplu cu un for loop și afișează fiecare element.
# animal=("leu","maimuta","gorila","girafa")
# for i in range(len(animal)):
#     print(animal[i])

# 2.Creează un tuplu cu 5 numere și afișează: suma numerelor, cel mai mare număr, cel mai mic număr
# numar=[3,5,7,8,1]
# print(sum(numar))
# print(max(numar))
# print(min(numar))

# 3.Verifică dacă un element există într-un tuplu.
# animal=("leu","maimuta","gorila","girafa")
# cuvant=input("Introdu cuvantul pe care il cauti: ")
# if cuvant in animal:
#     print("Cuvantul face parte din tuplu")
# else:
#     print("Cuvantul nu face parte din tuplu")

# 4.Ai următoarea listă de tupluri: studenti = [("Ana", 9), ("Mihai", 8), ("Ioana", 10)]. Afișează numele studentului cu cea mai mare notă.
# studenti = [("Ana", 9), ("Mihai", 8), ("Ioana", 10)]
# print(max(studenti, key=lambda x :x[1]))  #lambda x: x[1] înseamnă „ia doar al doilea element din fiecare tuplu”.

# 5.Creează o mică aplicație care gestionează contacte (nume + număr de telefon).
#Fiecare contact este un tuplu de forma (nume, telefon). Utilizatorul poate adăuga contacte până scrie „stop”
#La final: Afișează toate contactele. Permite căutarea unui contact după nume. 

agenda=[]
while True:
    contact=input("Adauga numele contactului: ")
    if contact.lower()=="stop":
        break
    numar=input("Adauga numarul de telefon: ")
    agenda.append((contact,numar))
print("Agenda completa este: ")
for contact, numar in agenda:
    print (f"{contact} -> {numar}")
nume=input("Introdu numele contactului cautat: ")
nume_gasit = False
for contact, numar in agenda:
    if contact.lower() == nume.lower():
        print(f"Numar: {numar}")
        nume_gasit = True
        break
else:
    print("Contactul nu a fost gasit.")

    