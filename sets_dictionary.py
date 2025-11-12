# Ai două liste de prieteni:
# prieteni_facebook = {"Ana", "Mihai", "Ioana", "Radu"}
# prieteni_instagram = {"Ioana", "Radu", "Elena"}
# Afișează persoanele comune
# Afișează prietenii care sunt doar pe Facebook
# Afișează prietenii care sunt doar pe Instagram
# Creează un set cu toți prietenii fără duplicate

prieteni_facebook = {"Ana", "Mihai", "Ioana", "Radu"}
prieteni_instagram = {"Ioana", "Radu", "Elena"}
prieteni_comuni=prieteni_facebook.intersection(prieteni_instagram)
print(prieteni_comuni)
doar_facebook=prieteni_facebook-prieteni_instagram
print(doar_facebook)
doar_instagram=prieteni_instagram-prieteni_facebook
print(doar_instagram)
toti_prietenii=prieteni_facebook|prieteni_instagram
print(toti_prietenii)

# Creează un catalog de note pentru mai mulți elevi (cheie = nume, valoare = listă de note).
# Calculează media fiecărui elev
# Afișează elevul cu cea mai mare medie

catalog={
    "Popescu": [8, 9, 10],
    "Amza":[6,10,5],
    "Lica": [7, 9, 5]
}

for elev, nota in catalog.items():
    medie=sum(nota)/len(nota)
    print(f"{elev} are media {medie:.2f}")

medii = {elev: sum(nota)/len(nota) for elev, nota in catalog.items()}
cel_mai_bun = max(medii, key=medii.get)
print(f"Elevul cu cea mai mare medie este {cel_mai_bun} ({medii[cel_mai_bun]:.2f})")
