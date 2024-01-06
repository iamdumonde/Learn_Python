allnumbers = [1, 2, 3, 4, 5, 6]
thirdElmt = allnumbers[2]
# print(thirdElmt)


allnames = ['Brian', 'Kim', 'Kam']

#append(): ajoute un élément à la fin de la liste
allnumbers.append(7)
allnames.append('Mummy')
# print(allnumbers)
# print(allnames)

#insert() : insère un élément à une position spécifique
allnumbers.insert(1, 10)
allnames.insert(3, 'Martin')
# print(allnumbers)
# print(allnames)

#remove(): supprime la première occurence d'un élément spécifié
new_list = ['univ', '4', '4', 'school']
new_list.remove('4')
# print(new_list)

#pop(): supprime l'élément à une position spécifique et le retourne
element_retire = new_list.pop(0)
# print(element_retire)

#Modification d'élément
new_list[0] = 9
# print(new_list)

#len():longueur d'un liste
longueur = len(new_list)
# print(longueur)

#concaténation de lists
ma_liste = [1, 3, 4]
autre_list = [7, 8, 9]
liste_concaténée = ma_liste + autre_list
# print(liste_concaténée)

#Exercice Pratique : Gestion de Notes
listnote_etudiant = []
listnote_etudiant.append(10)
listnote_etudiant.append(14)
listnote_etudiant.append(15)
listnote_etudiant.append(20)
listnote_etudiant.append(18)
listnote_etudiant.append(19)
listnote_etudiant[1] = 9
listnote_etudiant.pop(3)
listnote_etudiant.insert(1, 20)

studname = ['Marion', 'Usher', 'Chris', 'Marvel']
listnote_etudiant.extend(studname)
print(listnote_etudiant)
