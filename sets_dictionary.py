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
