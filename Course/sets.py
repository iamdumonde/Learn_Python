#Ensemble(set) est une collection non ordonnée d'éléments uniques. Les ensembles sont définis en utilisant des accolades {}
#Dans un ensemble (set) impossible de créer deux éléments, important de mettre des données uniques
new_set = {1, 2, 3, 4,"a", "b", "Mami", "NY"}
# print(new_set)

#accès aux éléments: étant non ordonnés le Set ne supporte pas l'indexation

#add()
new_set.add(True)
# print(new_set)

#remove(): supprimer un élément
new_set.remove('Mami')
# print(new_set)

#union()
another_set = {True, 'high', 1, 100}
union_set = new_set.union(another_set)
# print(union_set)

#inersection() : retourne les éléments communs à deux ensembles
intersection_set = new_set.intersection(another_set)
# print(intersection_set)

#Exercice Pratique
stud_course = ("HTML", "CSS", "JS", "PHP", "Laravel", "Nuxt")
all_courses_available = {"HTML", "CSS", "JS", "PHP", "Laravel", "Nuxt", "Angular", "Python", "Flutter", "Java", "SpringBoot"}
firststudcourse = stud_course[0]
courses_achieves = all_courses_available.remove("HTML")
all_courses_available.add("Sass")

#convert tuples
tuple_convert = list(stud_course)
tuple_convert[1] = "PCT"
tuple_convert_canceled = tuple(tuple_convert)
print(tuple_convert_canceled)
