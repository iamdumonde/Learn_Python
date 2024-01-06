#tuple est une structure de données similaire à une liste, mais immuable, inchangeable une fois qu'il a été créé
#impossible d'ajouter, supprimer ou modifier les élements après la création.
#possible d'effectuer des opérations telles que la concaténation ou la duplication

mon_tuple = (1, 2, 3, 'a', 'b')

#accès aux éléments
premier_element = mon_tuple[0]
first_stringelemnt = mon_tuple[3]
# print(premier_element, first_stringelemnt)

#Manipulation des Tuples en Python
#Duplication
tuple_dupl = mon_tuple * 3
print(tuple_dupl)