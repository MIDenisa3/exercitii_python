#                                                                           LISTE

# Creează o listă cu 5 fructe și afișează:
# -primul element
# -ultimul element
# -lungimea listei (len())
# -adaugă un fruct nou la final (append())
# -inserează un fruct pe poziția 2 (insert())
# -șterge un fruct din listă (remove() sau pop())

# mylist=["mere", "pere", "gutui", "lamai","struguri"]
# print("Primul element din lista este:", mylist[0])
# print("Ultimul element din lista este:", mylist[-1])
# print("Lungimea listei este:", len(mylist))
# mylist.append("pomelo")
# print(mylist)
# #mylist.insert(2,"cirese")
# #print(mylist)
# #mylist.pop(1)
# #print(mylist)

# Afișează elementele listei cu un for loop.

# for x in mylist:
#     print (x)

# Inversează o listă (cu reverse() sau slicing [::-1]).

# mylist.reverse()
# print(mylist)

# Ai lista numere = [4, 7, 2, 9, 1, 3].
# Sorteaz-o crescător și descrescător (sort(), sorted()).

# mylist=[4, 7, 2, 9, 1, 3]
# mylist.sort()
# print("Numerele in ordine crescatoare sunt:", mylist)
# mylist.sort(reverse = True)
# print("Numerele in ordine descrescatoare sunt:", mylist)

# Afișează suma tuturor numerelor (sum()).

# suma=sum(mylist)
# print("Suma numerelor este:", suma)

# # Afișează media lor aritmetică.

# medie=sum(mylist)/len(mylist)
# print("Media numerelor este:", medie)

# Creează o listă de 10 numere și afișează doar numerele pare.

# mylist=[10,11,12,13,14,15,16,17,18,19]
# for x in mylist:
#     if x % 2 == 0:
#         print("Numerele pare sunt: ", x)

# Din lista cuvinte = ["ana", "mere", "are", "pere", "dulci"], creează o listă nouă care conține numai cuvintele mai lungi de 3 litere.

# lista=["ana", "mere", "are", "pere", "dulci"]
# newlist=[x for x in lista if len(x)>3]
# print(newlist)

# Primești o listă de temperaturi în grade Celsius:
# Creează o listă nouă cu temperaturile în Fahrenheit.
# (formula: F = C * 9/5 + 32)

# temperaturi = [10, 15, 20, 25, 30]
# newlist=[x * 9/5 + 32 for x in temperaturi]
# print(newlist)

# Folosind list comprehension, generează o listă cu pătratele numerelor de la 1 la 10.

# mylist=[x for x in range(1,11)]
# print(mylist)
# newlist=[x**2 for x in range(1,11)]
# print(newlist)

# Creează o funcție pozitive(lista) care primește o listă de numere și returnează o listă cu doar cele pozitive.

# def pozitive(lista):
#     return [x for x in lista if x > 0]
# lista=[-2,3,4,-1,7,-9,10,11]
# # rezultat=pozitive(lista)
# # print(rezultat)

# Creează o funcție media_lista(lista) care primește o listă de numere și returnează media lor.

# def media_lista(lista):
#     if len(lista) == 0:
#         print("Lista este goala")
#         return None
#     return(sum(lista)/len(lista))
# lista=[1,2,3,4,5,6]
# rezultat=media_lista(lista)
# print(rezultat)

# Ai lista animale = ["pisica", "caine", "papagal", "elefant"].
# Creează o nouă listă care conține lungimea fiecărui cuvânt.

# animale=["pisica", "caine", "papagal", "elefant"]
# newlist=[len(x) for x in animale ]
# print(newlist)

# Ai două liste:
# nume = ["Ana", "Mihai", "Ioana"]
# varste = [23, 31, 19]
# Creează o listă de tupluri care combină numele cu vârstele lor, ex: [("Ana", 23), ("Mihai", 31), ...]

# nume=["Ana", "Mihai", "Ioana"]
# varste=[23,31,19]
# newlist=[(nume[x], varste[x]) for x in range(len(nume))]
# print(newlist)

# Creează o listă cu numere de la 1 la 5
# Creează o nouă listă în care fiecare număr este dublat

# lista=[1,2,3,4,5]
# newlist=[x*2 for x in lista]
# print(lista)
# print(newlist)

# Transformă lista de cuvinte în majuscule

# cuvinte = ["ana", "mere", "are", "pere"]
# newlist=[x.upper() for x in cuvinte]
# print(newlist)

# Creează un mic meniu de cumpărături:
# -utilizatorul introduce produse până tastează „stop”
# -la final, se afișează lista de cumpărături ordonată alfabetic

# meniu_de_cumparaturi=[]
# while True:
#     produs=input("Adauga ceva in lista (stop la final): ")
#     if produs.lower() == "stop":
#         break
#     meniu_de_cumparaturi.append(produs)
# meniu_de_cumparaturi.sort()
# print("Lista de cumparaturi:", meniu_de_cumparaturi)

# Verifică dacă o listă este palindrom, adică se citește la fel și invers (ex: [1, 2, 3, 2, 1] → True).
# lista=[1,2,3,3,2,1]
# if lista == lista[::-1]:                 #[::-1] creeaza lista inversata
#     print("Lista este palindrom")
# else:
#     print("Lista nu este palindrom")


# Lista de sarcini zilnice (To-Do List). Utilizatorul adaugă sarcini până tastează „gata”.
# La final, afișează:
# -lista completă
# -numărul de sarcini
# -sarcinile care încep cu o literă specificată (ex: „A”)

# lista_sarcini=[]
# while True:
#     sarcina=input("Adauga sarcina in lista (sau gata cand ai terminat):")
#     if sarcina.lower() == "gata":
#         break
#     lista_sarcini.append(sarcina)
# print("Sarcinile sunt:", lista_sarcini)
# print("Numarul de sarcini este:", len(lista_sarcini))
# litera=input("introdu litera pentru filtrare: ").lower()
# sarcini_filtrate=[s for s in lista_sarcini if s.lower().startswith(litera)]
# print("Sarcinile care incep cu litera ", litera, "sunt: ", sarcini_filtrate)

